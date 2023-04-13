import pandas as pd
file_path = 'sort1.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# 定义要查找的元素数组
element1 = ['A', 'B', 'C']

# 选择你要提取的列名，例如 'Make'
column_name = 'Make'

# 根据element1数组筛选数据
filtered_df = df[df[column_name].isin(element1)]

# 将筛选后的数据保存到新的Excel文件
output_file_path = 'filtered_excel_file.xlsx'
filtered_df.to_excel(output_file_path, index=False, engine='openpyxl')

print(f"已将筛选后的数据保存到 {output_file_path}。")
