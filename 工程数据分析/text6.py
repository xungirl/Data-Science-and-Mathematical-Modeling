import pandas as pd
import matplotlib.pyplot as plt
#import numpy as np
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')
target_variable = df['A']  # 请将 'Target' 替换为目标变量所在列的列名
num_features = 9
feature_names = ['Thickness','Milling depth','Perception','Freeze Index','Structual number','kESAL','Age','A_pre','TN_pre']
plt.figure(figsize=(15, 15))

for i in range(num_features):
    plt.subplot(3, 3, i+1)
    x = df[feature_names[i]]
    y = target_variable
    
    # 绘制散点图
    plt.scatter(x, y, s=20, marker='o', color='green')
    


    plt.xlabel(feature_names[i])
    plt.ylabel('Target')

plt.tight_layout()
plt.show()




