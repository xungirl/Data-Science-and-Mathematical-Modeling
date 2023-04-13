import pandas as pd
file_path = 'origin2_end.xlsx'# read the excel
df = pd.read_excel(file_path,engine='openpyxl')
# Select the column name you want to count
column_name = 'Make'
element_counts = df[column_name].value_counts().reset_index()
element_counts.columns = [column_name, 'count']
# Merge raw data with counting results
df_merged = df.merge(element_counts, on=column_name)
# Sort in descending order based on counting results
df_sorted = df_merged.sort_values(by='count', ascending=False)
output_file_path = 'origin22_end.xlsx'
df_sorted.to_excel(output_file_path, index=False, engine='openpyxl')
print(f"{output_file_path}。")
