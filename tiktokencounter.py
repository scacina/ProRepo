import os
import sys
import argparse
import tiktoken
import pdfplumber
import fitz
import PyPDF2



def count_tokens_tiktoken(text, model="gpt-4"):
    """
    Count tokens in the text using tiktoken for the specified model.
    """
    encoding = tiktoken.encoding_for_model(model)
    tokens = encoding.encode(text)
    return len(tokens)

def get_pdf_text(file_path):
    """
    Extract text from a PDF file using PyPDF2.
    """
    text = ""
    with open(file_path, "rb") as f:
        pdf_reader = PyPDF2.PdfReader(f)
        for page in pdf_reader.pages:
            extracted = page.extract_text()
            if extracted:  # Check if text was successfully extracted
                text += extracted + " "
    token_count = count_tokens_tiktoken(text)
    print(f"Token count using model PyPDF2: {token_count}")
    return text

def get_pdf_text_pdffitz(file_path):   
    text = ""
    # Open the PDF file
    with fitz.open(file_path) as doc:
        # Iterate through each page
        for page in doc:
            # Extract text from the current page
            text += page.get_text()
    token_count = count_tokens_tiktoken(text)
    print(f"Token count using model pdffitz: {token_count}")
    return text
    
def get_pdf_text_pdfplumber(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            # extract_text() returns None if no text is found, so we safeguard against that
            extracted = page.extract_text()
            if extracted:
                text += extracted + " "
    token_count = count_tokens_tiktoken(text)
    print(f"Token count using model pdfplumber: {token_count}")
    return text

def get_txt_text(file_path):
    """
    Read text from a TXT file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()
    token_count = count_tokens_tiktoken(text)
    print(f"Token count using model get_txt_text: {token_count}")
    return text

def main(file_path, model):
    # Determine file extension
    ext = os.path.splitext(file_path)[1].lower()
    textplumber = 0
    if ext == ".pdf":
        get_pdf_text_pdffitz(file_path)
        #get_pdf_text_pdfplumber(file_path)
        #get_pdf_text(file_path)
    elif ext == ".txt":
        text = get_txt_text(file_path)
    else:
        print("Unsupported file type. Only .pdf and .txt files are supported.")
        return



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get token count for PDF and TXT files using tiktoken")
    parser.add_argument("file", help="Path to the file (.pdf or .txt)")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="Model name to use for tiktoken (default: gpt-3.5-turbo)")
    args = parser.parse_args()
    main(args.file, args.model)
