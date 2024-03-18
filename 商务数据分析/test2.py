import pandas as pd
import numpy as np

# 读取本地 Excel 文件
input_file = 'dataorigin.xlsx'  # 请将此处替换为您的实际文件名
df = pd.read_excel(input_file)

# 数据预处理
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)

# 将处理后的数据导入到一个名为 'data' 的 Excel 表中
output_file = 'data.xlsx'
with pd.ExcelWriter(output_file) as writer:
    df.to_excel(writer, index=False, sheet_name='data')