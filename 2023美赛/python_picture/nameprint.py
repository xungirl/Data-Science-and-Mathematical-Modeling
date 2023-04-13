import pandas as pd
# read excel
file_path = 'sort2.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')
column_name = 'Make'
column_data = df[column_name].tolist()
unique_elements = []
for item in column_data:
    if item not in unique_elements:
        unique_elements.append(item)
print(f"\n{unique_elements}")
count = 0
for name in unique_elements:
    count = count+1
print(f"There are a total of {count}elements")
element1=unique_elements[0:10]
df = pd.read_excel(file_path, engine='openpyxl')
# Select the column name you want to extract
column_name = 'Make'
# Filter data based on the element1 array
filtered_df = df[df[column_name].isin(element1)]
output_file_path = 'twotop10.xlsx'
filtered_df.to_excel(output_file_path, index=False, engine='openpyxl')
print(f" {output_file_path}。")

