import os
import json
import pdfplumber
import pandas as pd
import PyPDF2

def extract_tables_from_pdf(pdf_path):
    tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                df = pd.DataFrame(table[1:], columns=table[0])
                tables.append(df.to_dict(orient='records'))
    return tables

def process_pdfs_in_folder(folder_path):
    all_tables = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            tables = extract_tables_from_pdf(pdf_path)
            all_tables[filename] = tables
    return all_tables

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    folder_path = 'pdfs'
    output_file = 'output.json'
    
    all_tables = process_pdfs_in_folder(folder_path)
    save_to_json(all_tables, output_file)

    print(f"Tables extracted and saved to {output_file}")