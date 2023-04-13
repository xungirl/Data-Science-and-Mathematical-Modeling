import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

# 读取Excel文件
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# 从DataFrame中选择自变量（X）和因变量（y）
X = df[['Thickness', 'Milling depth', 'Perception', 'Freeze Index','Structual number','Age']]
y = df['TN']

# 定义测试集大小范围和R²值列表
#test_sizes=0.18
test_sizes = np.arange(0.1, 1.0, 0.02)
r2_scores = []

# 对于每个测试集大小，训练模型并计算R²值
for test_size in test_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    y_pred = reg.predict(X_test)
    r2 = r2_score(y_test, y_pred)
    r2_scores.append(r2)

# 找到R²值最大的点的索引
max_r2_index = np.argmax(r2_scores)
max_r2_test_size = test_sizes[max_r2_index]
max_r2_score = r2_scores[max_r2_index]


# 绘制test_size和R²值之间的关系图，除最大值点外其他点为蓝色
plt.plot(test_sizes, r2_scores, marker='o', color='blue', label='R² Scores')
plt.scatter(max_r2_test_size, max_r2_score, marker='o', color='#DB7093', label='Max R² Score')

# 在最大R²值点处添加横纵坐标文本注释
plt.annotate(f"({max_r2_test_size:.2f}, {max_r2_score:.2f})", (max_r2_test_size, max_r2_score), textcoords="offset points", xytext=(-10,7), ha='center',fontsize=8,color='red')
plt.xlabel('Test Size')
plt.ylabel('R² Score')
plt.title('R² Score vs Test Size')
plt.grid()
plt.legend()
plt.show()

