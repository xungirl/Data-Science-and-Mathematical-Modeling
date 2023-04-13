import pandas as pd
import numpy as np
import seaborn as sns
data = pd.read_excel("data.xlsx")
data.head()
#查看数据集中样本数量和特征数量
data.shape
#查看数据信息，检查是否有缺失值
data.info() 
data.describe()
#连续特征之间的散点图
sns.pairplot(data,hue='sex',)