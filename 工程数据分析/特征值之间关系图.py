import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt
excel_file = 'outputone.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl',skiprows=[0])
columns_to_analyze = df.columns[:9]
X = df[columns_to_analyze]
# 设置绘图区域大小
plt.figure(figsize=(12, 12))

# 绘制散点图矩阵
for i in range(len(columns_to_analyze)):
    for j in range(len(columns_to_analyze)):
        plt.subplot(len(columns_to_analyze), len(columns_to_analyze), i * len(columns_to_analyze) + j + 1)
        if i != j:
            plt.scatter(X.iloc[:, i], X.iloc[:, j], c=['#3CB371'], s=10, edgecolor='w')
        else:
            plt.text(0.5, 0.5, columns_to_analyze[i], horizontalalignment='center', verticalalignment='center')
        plt.gca().set_xticks([])
        plt.gca().set_yticks([])
plt.tight_layout()
plt.show()
