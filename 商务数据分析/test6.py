import pandas as pd

# 假设数据集存储在一个名为data.csv的文件中
data = pd.read_csv('vgsales.csv')

# 计算各游戏类型的销售额统计量
game_type_stats = data.groupby('Genre')['Global_Sales'].agg(['sum', 'mean', 'median', pd.Series.mode])

# 计算各平台的销售额统计量
platform_stats = data.groupby('Platform')['Global_Sales'].agg(['sum', 'mean', 'median', pd.Series.mode])

# 计算各地区市场的销售额统计量
# 假设数据集中有三个地区：NA_Sales, EU_Sales, JP_Sales
region_sales = ['NA_Sales', 'EU_Sales', 'JP_Sales']
region_stats = data[region_sales].agg(['sum', 'mean', 'median', pd.Series.mode])

print("Game Type Sales Stats:\n", game_type_stats)
print("\nPlatform Sales Stats:\n", platform_stats)
print("\nRegion Sales Stats:\n", region_stats)