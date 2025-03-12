import streamlit as st
import mysql.connector
import os
from task1 import extract_pdf
from task2 import extract_interest_regions
from ocr import process_all_folders
import pandas as pd
from config import DB_CONFIG

# Disable Streamlit's file watcher to avoid PyTorch conflict
#st.set_option('server.fileWatcherType', 'none')

# Streamlit UI for PDF Upload
st.title("Automated Bank Check Extraction")
uploaded_pdf = st.file_uploader("Upload a PDF", type=["pdf"])

if uploaded_pdf is not None:
    # Save the uploaded PDF
    pdf_path = os.path.join("uploaded_pdfs", uploaded_pdf.name)
    os.makedirs("uploaded_pdfs", exist_ok=True)
    with open(pdf_path, "wb") as f:
        f.write(uploaded_pdf.read())
    st.success("PDF uploaded successfully!")

    # Step 1: Extract images from PDF
    output_folder = "task1_output"
    extract_pdf(pdf_path, output_folder, width=1000, height=600)
    st.info("Images extracted from PDF.")

    # Step 2: Extract regions of interest
    regions_output_folder = "task2_output"
    regions_of_interest = {
        'date': (754, 40, 970, 88),
        'payee': (70, 120, 760, 175),
        'name': (825, 440, 990, 475),
        'amount_digits': (735, 225, 970, 290),
        'account_number': (115, 300, 320, 335)
    }
    extract_interest_regions(output_folder, regions_of_interest, regions_output_folder)
    st.info("Regions of interest extracted.")

    # Step 3: Perform OCR and store results in MySQL
    output_csv = "extracted_data.csv"
    process_all_folders(regions_output_folder, output_csv)

    # Debug: Check if extracted CSV is generated
    if os.path.exists(output_csv):
        st.success("OCR results saved to CSV.")
    else:
        st.error("OCR results CSV not found!")

    # Debug: Check MySQL connection
    conn = mysql.connector.connect(**DB_CONFIG)
    if conn.is_connected():
        st.success("Connected to MySQL database.")
    else:
        st.error("Failed to connect to MySQL database.")
    
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS check_data (
            id INT AUTO_INCREMENT PRIMARY KEY,
            folder VARCHAR(255),
            date TEXT,
            payee TEXT,
            name TEXT,
            amount_digits TEXT,
            account_number TEXT
        )
    """)

    # Load OCR results from CSV
    df = pd.read_csv(output_csv)
    
    # Debug: Display DataFrame content before insertion
    st.subheader("Data to be Inserted into Database")
    st.dataframe(df)

    for _, row in df.iterrows():
        # Debug: Print each row's data before insertion
        print(row['Folder'], row.get('date_region', ''), row.get('payee_region', ''),
              row.get('name_region', ''), row.get('amount_digits_region', ''),
              row.get('account_number_region', ''))

        cursor.execute("""
            INSERT INTO check_data (folder, date, payee, name, amount_digits, account_number) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            row['Folder'],
            row.get('date_region', ''),
            row.get('payee_region', ''),
            row.get('name_region', ''),
            row.get('amount_digits_region', ''),
            row.get('account_number_region', '')
        ))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("OCR results saved to MySQL database.")

    # Display extracted data from CSV
    st.subheader("Extracted Data")
    st.dataframe(df)
