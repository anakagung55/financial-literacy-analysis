import pandas as pd


file_path = 'C:/Users/62877/Desktop/KKN/Desa Bunutin - Bangli (Jawaban).xlsx'

df = pd.read_excel(file_path, sheet_name='Form Responses 1')


relevant_columns = {
    "pinjol_usage": "Apakah Anda pernah meminjam uang dari Pinjaman Online (Pinjol)?",
    "check_pinjol_legality": "Apakah Anda mengetahui cara mengecek legalitas suatu Pinjaman Online (Pinjol)?",
    "victim_pinjol_illegal": "Apakah Anda pernah menjadi korban Pinjaman Online (Pinjol) Ilegal?",
    "distinguish_legal_illegal_investment": "Apakah Anda paham cara membedakan investasi yang legal dan ilegal?",
    "know_illegal_investment": "Apakah Anda pernah mendengar/mengetahui adanya aktivitas investasi ilegal/bodong di desa Anda?"
}


percentages = {}
for key, column in relevant_columns.items():
    total_responses = len(df)
    affirmative_responses = df[column].str.lower().str.contains("ya").sum()
    percentage = (affirmative_responses / total_responses) * 100
    percentages[key] = percentage

# Print the results
for key, value in percentages.items():
    print(f"{key}: {value:.2f}%")
