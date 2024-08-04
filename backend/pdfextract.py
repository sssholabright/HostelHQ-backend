import pdfplumber
import tabula
import pandas as pd

# Extract text using pdfplumber
pdf_text = ""
with pdfplumber.open('Mobile_Application_Architectures.pdf') as pdf:
    for page in pdf.pages:
        pdf_text += page.extract_text() or ""

# Extract tables using tabula
tables = tabula.read_pdf('Mobile_Application_Architectures.pdf', pages='all', multiple_tables=True)

# Save extracted text to a CSV file
text_file_path = 'extracted_tessxt.csv'
with open(text_file_path, 'w', newline='', encoding='utf-8') as text_file:
    text_file.write(pdf_text)

# Save tables to separate CSV files
for i, table in enumerate(tables):
    table_file_path = f'table_{i}.csv'
    table.to_csv(table_file_path, index=False)

print(f"Text saved to {text_file_path}")
print(f"Tables saved to table_0.csv, table_1.csv, ...")



"""import pdfplumber
import pandas as pd

with pdfplumber.open('Adejobi_Mujeeb_Oyinade_Result_Slip.PDF') as pdf:
    all_text = ''
    tables_plumber = []

    for page in pdf.pages:
        all_text += page.extract_text()
        tables_plumber.extend(page.extract_tables())

    rows = []

    rows.append(['Text Section'])
    rows.append([all_text])
    rows.append([])


    rows.append(['Table Section'])
    for i, table in enumerate(tables_plumber):
        df = pd.DataFrame(table[1:], columns=table[0])
        df.insert(0, 'source', f'Table (pdfplumber) {i}')
        rows.append(df.columns.tolist())
        rows.extend(df.values.tolist())
        rows.append([])


df_combined = pd.DataFrame(rows)

df_combined.to_csv('output.csv', index=False, header=False)
"""        
    
