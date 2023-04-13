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

test_sizes = np.arange(0.1, 1.0, 0.02)
r2_scores = []

for test_size in test_sizes:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    lasso_model = Lasso(alpha=1.0)
    lasso_model.fit(X_train, y_train)
    
    y_pred = lasso_model.predict(X_test)
    
    r2 = r2_score(y_test, y_pred)
    r2_scores.append(r2)

max_r2 = max(r2_scores)
max_r2_index = r2_scores.index(max_r2)
max_test_size = test_sizes[max_r2_index]

plt.plot(test_sizes, r2_scores, marker='o', label='R^2 Score')
plt.scatter(max_test_size, max_r2, color='red', label=f'Max R^2 ({max_test_size:.1f}, {max_r2:.2f})')
plt.xlabel("Test Size")
plt.ylabel("R^2 Score")
plt.title("Test Size vs R^2 Score")
plt.legend()
plt.grid()
plt.show()

print(f"Maximum R^2 score in the given interval: {max_r2:.2f}")


