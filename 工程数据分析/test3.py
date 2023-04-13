import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def adjusted_r2(r2, n, p):
    return 1 - (1 - r2) * (n - 1) / (n - p - 1)

# 读取Excel文件
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

# 从DataFrame中选择自变量（X）和因变量（y）
X = df[['Thickness', 'Milling depth', 'Perception', 'Freeze Index','Structual number','Age']]
y = df['TN']
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.18, random_state=42)

# 构建回归模型并进行拟合
reg = LinearRegression()
reg.fit(X_train, y_train)

# 预测
y_pred = reg.predict(X_test)

# 计算决定系数（R²）
r2 = r2_score(y_test, y_pred)

# 计算校正回归系数（Adjusted R²）
n = len(y_test)
p = X_train.shape[1]
adj_r2 = adjusted_r2(r2, n, p)

print(f"R²: {r2:.3f}")
print(f"Adjusted R²: {adj_r2:.3f}")
