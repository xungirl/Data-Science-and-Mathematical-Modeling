import pandas as pd
#import numpy as np

# 读取数据集
url = "https://raw.githubusercontent.com/GregorUT/videogamesales/master/vgsales.csv"
df = pd.read_csv(url)

# 数据预处理
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Year'] = df['Year'].astype(int)

# 将处理后的数据导入到一个新的 Excel 表中
output_file = 'data.xlsx'
df.to_excel(output_file, index=False)