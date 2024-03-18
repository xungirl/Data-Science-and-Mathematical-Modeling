import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv(r'vgsales.csv')
data.head()
data.pivot_table(index ='Year',values=['NA_Sales','EU_Sales','JP_Sales','Other_Sales'],aggfunc='sum').plot(figsize=(10,6))
plt.grid()
plt.ylabel('/million')
