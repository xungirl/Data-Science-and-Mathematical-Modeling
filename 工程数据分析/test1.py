import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 读取Excel文件
excel_file = 'outputone.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# 从DataFrame中选择自变量（X）和因变量（y）
X = df[['A','B','C','D','E','F','G','H'	,'I']]
y = df['TN']

# 将数据拆分为训练集和测试集（测试集占30%）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.12, random_state=42)

# 创建线性回归模型并拟合
reg = LinearRegression()
reg.fit(X_train, y_train)

# 预测测试集
y_pred = reg.predict(X_test)

# 计算并打印评估指标
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R² Score: {r2}")
