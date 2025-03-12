**Automating Bank Check Extraction from Scanned PDFs (Feb 2025)**

**Project Overview**

This project automates the extraction of information from scanned bank checks using Optical Character Recognition (OCR) technology. It utilizes Streamlit for the user interface, Google Gemini API for OCR processing, and MySQL for structured data storage. The system efficiently processes scanned PDFs, extracts relevant details, and stores them in a database, enhancing accuracy and operational efficiency.

**Output**


![image_alt](https://github.com/Springboard-Internship-2024/Automating-Bank-Check-Extraction-from-Scanned-PDFs_Feb_2025/blob/nagabhushanarao/Screenshot%202025-02-27%20131458.png?raw=true)

![image_alt](https://github.com/Springboard-Internship-2024/Automating-Bank-Check-Extraction-from-Scanned-PDFs_Feb_2025/blob/nagabhushanarao/Screenshot%202025-02-27%20132011.png?raw=true)

**Features**
PDF Upload and Processing: Users can upload scanned PDFs through a Streamlit-based interface.
OCR Analysis: Utilizes Google Gemini API for accurate text extraction from check images.
Data Storage: Extracted data is stored in a MySQL database for easy retrieval and analysis.
Modular Design: Organized tasks for image extraction and OCR processing.

**Tech Stack**
Programming Language: Python
Framework: Streamlit
OCR Service: Google Gemini API
Database: MySQL
Other Libraries: OpenCV, PyPDF2, Pandas, SQLAlchemy

**Project Structure**

Automating-Bank-Check-Extraction-from-Scanned-PDFs_Feb_2025/
│

├── .streamlit/             # Streamlit configuration

├── task1_output/           # Output from task1.py

├── task2_output/           # Output from task2.py

├── temp/                   # Temporary files for processing

├── uploaded_pdfs/          # Uploaded PDFs from users

├── venv/                   # Virtual environment

├── __pycache__/            # Compiled Python files

│
├── app.py                  # Main Streamlit application

├── config.py               # Configuration file (API keys, DB credentials)

├── extracted_data.csv      # (Optional) Backup storage of extracted data

├── ocr.py                  # Handles OCR processing using Google Gemini API

├── task1.py                # Task 1: Image extraction from PDF

├── task2.py                # Task 2: OCR processing on extracted images

└── README.md               # Project documentation


**Usage**
Upload PDF: Navigate to the Streamlit app and upload a scanned PDF of a bank check.
Image Extraction: Images are extracted from the uploaded PDF (task1.py).
OCR Processing: Text is extracted from the images using Google Gemini API (ocr.py and task2.py).
Data Storage: Extracted data is stored in the MySQL database (check_data table).
Output: View and analyze extracted data on the Streamlit dashboard.

**Future Enhancements**
Implementing advanced data validation and error handling mechanisms.
Adding support for additional OCR engines for enhanced accuracy.
Expanding the visualization dashboard with more insights and metrics.
Integrating machine learning for check fraud detection and signature verification.

**Acknowledgments**
Google Gemini API for the powerful OCR capabilities.
Streamlit for the interactive and user-friendly UI framework.
MySQL for the efficient database management system.

**Contact**
For any questions or suggestions, please reach out to:
G.Nagabhushanarao
LinkedIn: www.linkedin.com/in/gujjidi-nagabhushanarao-0ba361277

