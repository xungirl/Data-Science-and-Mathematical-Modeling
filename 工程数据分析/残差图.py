import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')

feature_names = ['Thickness','Milling depth','Perception','Freeze Index','Structual number','kESAL','Age','A_pre','TN_pre']
target_column = 'A'  # 请将 'Target' 替换为目标变量所在列的列名

X = df[feature_names]
y = df[target_column]

X.fillna(X.mean(), inplace=True)
y.fillna(y.mean(), inplace=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

lasso_model = Lasso(alpha=1.0)
lasso_model.fit(X_train, y_train)

y_pred_train = lasso_model.predict(X_train)
y_pred_test = lasso_model.predict(X_test)

residuals_train = y_train - y_pred_train
residuals_test = y_test - y_pred_test

plt.scatter(y_pred_train, residuals_train, color='blue', alpha=0.5, label='Training Set')
plt.scatter(y_pred_test, residuals_test, color='red', alpha=0.5, label='Test Set')
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.legend()
plt.grid()
plt.show()
