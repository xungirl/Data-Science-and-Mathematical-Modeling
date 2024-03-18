
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')
columns_to_analyze = df.columns[1:11]
X = df[columns_to_analyze]
correlation_matrix = X.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(correlation_matrix, annot=True, cmap="YlGn", vmin=-1, vmax=1)
plt.title("Correlation coefficient matrix thermal diagram")
plt.show()
#相关系数矩阵热力图