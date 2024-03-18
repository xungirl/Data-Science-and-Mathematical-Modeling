import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 加载数据集
data = pd.read_excel('data.xlsx', engine='openpyxl')  # 请替换为您的数据集路径

# 特征选择（根据前面的特征排名结果）
selected_features = ['NA_Sales', 'EU_Sales']  # 请替换为您的重要特征
X = data[selected_features]
y = data['Global_Sales']  # 请替换为您的目标变量

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建随机森林模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)

# 训练模型
rf.fit(X_train, y_train)

# 进行预测
y_pred = rf.predict(X_test)

# 评估预测结果
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error: {:.6f}".format(mse))
print("R² Score: {:.6f}".format(r2))