import pandas as pd

# Load the Excel file
file_path = 'C:/Users/62877/Desktop/KKN/Desa Bunutin - Bangli (Jawaban).xlsx'
df = pd.read_excel(file_path, sheet_name='Form Responses 1')

# Define a function to categorize addresses
def categorize_address(address):
    address = address.lower()
    if 'bunutin' in address:
        return 'Banjar Bunutin'
    elif 'selati' in address:
        return 'Banjar Selati'
    elif 'dukuh' in address:
        return 'Banjar Dukuh'
    elif 'guliang' in address:
        return 'Banjar Guliang Kawan'
    elif 'dadia' in address:
        return 'Banjar Dadia Puri'
    else:
        return 'Other'

# Apply the categorization function to the 'Alamat' column
df['Banjar'] = df['Alamat'].apply(categorize_address)

# Save the updated DataFrame to a new Excel file
output_path = 'C:/Users/62877/Desktop/KKN//Desa_Bunutin_Categorized.xlsx'
df.to_excel(output_path, index=False)

print("Categorization complete. The file has been saved as 'Desa_Bunutin_Categorized.xlsx'")
