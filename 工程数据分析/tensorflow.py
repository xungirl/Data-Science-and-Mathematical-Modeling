import pandas as pd
import numpy as np
from tensorflow import keras
from tensorflow import keras as kr
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score

# 1. 读取Excel文件
data = pd.read_excel("data.xlsx")

# 2. 处理缺失值：用平均值代替
data.fillna(data.mean(), inplace=True)

# 3. 划分数据集为特征和目标变量
X = data.iloc[:, :-1]  # 取前8个特征
y = data.iloc[:, -1]   # 取最后一个特征作为目标变量

# 4. 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. 标准化数据
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 6. 构建神经网络模型
model = Sequential()
model.add(Dense(32, activation='relu', input_shape=(9,)))
model.add(Dense(16, activation='relu'))
model.add(Dense(1, activation='linear'))

# 7. 编译和训练模型
model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)

# 8. 预测并计算R方
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print("R-squared (R2):", r2)
