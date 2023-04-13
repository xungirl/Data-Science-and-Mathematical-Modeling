import pandas as pd
file_path = 'new_Catamarans.xlsx'
df = pd.read_excel(file_path,sheet_name='Sheet1', engine='openpyxl')
# Eliminate prefix and suffix spaces for all elements
df_trimmed = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)
output_file_path = 'new_Catamarans.xlsx'
df_trimmed.to_excel(output_file_path, index=False, engine='openpyxl')
print(f"{output_file_path}。")
