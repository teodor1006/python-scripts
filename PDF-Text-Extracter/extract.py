# pip install PyPDF2
import PyPDF2
import os

# Get the directory of the current script
script_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the PDF file
pdf_file_path = os.path.join(script_directory, 'Abstract_English.pdf')

# Open the PDF file using a context manager
with open(pdf_file_path, 'rb') as pdfFileObj:
    # Create a PDF reader object
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # Print the number of pages
    num_pages = len(pdfReader.pages)
    print(f"Number of pages: {num_pages}")

    # Extract text from the first page
    pageObj = pdfReader.pages[0]
    text = pageObj.extract_text()

    print(text)


