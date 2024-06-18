import pandas as pd

# Load the corrected CSV file with comma as the delimiter
file_path_corrected = 'focos_br_ref_2004.csv'
df = pd.read_csv(file_path_corrected, delimiter=',')

# Save the dataframe to an Excel file
output_excel_file = 'focos_br_ref_2004_corrected.xlsx'
df.to_excel(output_excel_file, index=False, engine='openpyxl')

print(f"CSV file has been fixed and saved as {output_excel_file}")
