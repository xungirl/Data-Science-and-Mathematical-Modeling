import pandas as pd
import numpy as np

def normalization_needed(dataframe, threshold=4):
    max_values = dataframe.max()
    min_values = dataframe.min()
    
    ratios = max_values / min_values

    if any(ratios > threshold):
        return True
    else:
        return False

def choose_normalization_method(dataframe):
    if dataframe.skew().abs().mean() > 2:
        return "Log transformation"
    else:
        return "MinMaxScaler"

# 读取Excel文件
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# 假设前4列为自变量
X = df.iloc[:, :9]

if normalization_needed(X):
    normalization_method = choose_normalization_method(X)
    print(f"归一化处理是必要的，建议使用 {normalization_method}")
else:
    print("数据无需归一化处理")
