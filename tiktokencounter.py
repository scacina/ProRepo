import os
import sys
import argparse
import tiktoken
from transformers import AutoTokenizer


try:
    import PyPDF2
except ImportError:
    print("PyPDF2 is required for PDF processing. Install it using 'pip install PyPDF2'")
    sys.exit(1)
    
    



def transformers_tokenize(text):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased") # Example: BERT tokenizer
    tokens = tokenizer.tokenize(text) # Or tokenizer.encode(text, add_special_tokens=False) for token IDs
    token_count_transformers = len(tokens)
    print(f"Transformers token count (BERT): {token_count_transformers}")

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
    return text

def get_txt_text(file_path):
    """
    Read text from a TXT file.
    """
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def main(file_path, model):
    # Determine file extension
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        text = get_pdf_text(file_path)
    elif ext == ".txt":
        text = get_txt_text(file_path)
    else:
        print("Unsupported file type. Only .pdf and .txt files are supported.")
        return

    transformers_tokenize(text)
    token_count = count_tokens_tiktoken(text, model)
    print(f"Token count using model '{model}': {token_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get token count for PDF and TXT files using tiktoken")
    parser.add_argument("file", help="Path to the file (.pdf or .txt)")
    parser.add_argument("--model", default="gpt-3.5-turbo", help="Model name to use for tiktoken (default: gpt-3.5-turbo)")
    args = parser.parse_args()
    main(args.file, args.model)
