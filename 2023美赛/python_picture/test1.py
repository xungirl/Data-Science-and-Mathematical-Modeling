#散点图绘制
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data.xlsx')
plt.scatter( df.iloc[:, 0],df.iloc[:, 1],c='#FF8C00')
plt.xlabel('Length')
plt.ylabel('Listing Price')

plt.show()