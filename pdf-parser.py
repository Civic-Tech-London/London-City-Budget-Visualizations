import os
import json
import pdfplumber
import pandas as pd

def extract_tables_from_pdf(pdf_path):
    tables = "";
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            extracted_tables = page.extract_tables()
            for table in extracted_tables:
                df = pd.DataFrame(table[2:], columns=table[0])
                tables=(df.to_dict(orient='records'))
    return tables

def extract_data(keyphrase,pdf_path):

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if keyphrase in text:
                keyphrase_pos = text.find(keyphrase)
                if keyphrase_pos != -1:
                    extracted_text = text[:keyphrase_pos]
                    # extracted_text[extracted_text.find("$"),extracted_text.find("%")]
                    startpos = extracted_text.find("$")
                    endpos = (extracted_text.find("%")+1)
                    extracted_text = extracted_text[startpos:endpos]
                    extracted_text = extracted_text.split()
                    print(extracted_text)
                    return extracted_text
        
        return "not_found"

def process_pdfs_in_folder(folder_path):
    all_tables = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            tables = extract_tables_from_pdf(pdf_path)
            # costPerDay = extract_cost_per_day()
            overview = extract_data( "Cost per day for the",pdf_path)
            if(len(overview) == 2):
                all_tables.append({"service":filename,
                "cost-per-day": overview[0], #extract_data( "Cost per day for the",pdf_path),
                "net-prop-supported-budget-percentage": overview[1], #extract_data( "Cost per day for the average rate payer",pdf_path),
                "budget": tables})
            
            else:
                all_tables.append({"service":filename,
                "cost-per-day":"unknown", #extract_data( "Cost per day for the",pdf_path),
                "net-prop-supported-budget-percentage": "unknown", #extract_data( "Cost per day for the average rate payer",pdf_path),
                "budget": tables})

    return all_tables

def save_to_json(data, output_file):
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    folder_path = 'pdfs/' #update to match your path
    output_file = 'output.json' #update to match your path

    print(f"running process_pdfs_in_folder() function")
    
    all_tables = process_pdfs_in_folder(folder_path)
    save_to_json(all_tables, output_file)

    print(f"Tables extracted and saved to {output_file}")
