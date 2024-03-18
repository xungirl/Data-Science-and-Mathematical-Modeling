import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

# 1. 加载数据
data = pd.read_excel('data.xlsx', engine='openpyxl')

# 2. 数据预处理
# 删除缺失值
data = data.dropna()

# 独热编码
encoder = OneHotEncoder(sparse=False)
categorical_features = ['NA_Sales', 'EU_Sales', 'Publisher']
encoded_features = encoder.fit_transform(data[categorical_features])
encoded_features_df = pd.DataFrame(encoded_features, columns=encoder.get_feature_names(categorical_features))

# 将独热编码后的特征与原始数据合并
data = data.reset_index(drop=True)
data = pd.concat([data.drop(categorical_features, axis=1), encoded_features_df], axis=1)

# 划分训练集和测试集
X = data.drop(['Rank', 'Name', 'Year', 'Global_Sales'], axis=1)
y = data['Global_Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 训练随机森林模型
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 4. 评估模型
y_pred = rf.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Mean Squared Error:', mse)
print('R² Score:', r2)

# 5. 特征重要性
importances = rf.feature_importances_
indices = np.argsort(importances)[::-1]

print('Feature ranking:')
for f in range(X.shape[1]):
    print('%d. feature %s (%f)' % (f + 1, X.columns[indices[f]], importances[indices[f]]))