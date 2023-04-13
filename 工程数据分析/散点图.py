import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
excel_file = 'data.xlsx'
df = pd.read_excel(excel_file, engine='openpyxl')
x_data = df['Age']
y_data = df['A']
coefficients = np.polyfit(x_data, y_data, deg=1)
trendline = np.poly1d(coefficients)
y_pred = trendline(x_data)
plt.scatter(x_data, y_data, label='Data points',s=5, marker='o',color='green')
plt.plot(x_data, y_pred, color='red', label='Trendline')
plt.xlabel('A')
plt.ylabel('B')
plt.legend()
plt.show()
