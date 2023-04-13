import pandas as pd
import plotly.graph_objects as go
import numpy as np 

# 读取Excel文件中的两个表格
file_path1 = 'origin1_end.xlsx'
file_path2 = 'origin2_end.xlsx'
df1 = pd.read_excel(file_path1,engine='openpyxl')
df2 = pd.read_excel(file_path2,engine='openpyxl')

# 提取x和y轴的数据
x1 = df1['Year']
y1 = df1['Listing Price']
x2 = df2['Year']
y2 = df2['Listing Price']

# 计算趋势线
z1 = np.polyfit(x1, y1, 1)
p1 = np.poly1d(z1)
z2 = np.polyfit(x2, y2, 1)
p2 = np.poly1d(z2)

# 创建散点图
fig = go.Figure()

# 添加第一个表格的散点数据和趋势线
fig.add_trace(go.Scatter(x=x1, y=y1, mode='markers',name='Monohulled Sailboats',marker=dict(color='#ff9d00', size=12,opacity=0.7,),line=dict(width=3, color='black')))
fig.add_trace(go.Scatter(x=x1, y=p1(x1), mode='lines', name='Monohulled SailboatsTrendline',line=dict(color='#ff9d00', width=2)))
# 添加第二个表格的散点数据和趋势线
fig.add_trace(go.Scatter(x=x2, y=y2, mode='markers',name='Catamarans',marker=dict(color='#2e9db1', size=12,opacity=0.5,),line=dict(width=3, color='black')))
fig.add_trace(go.Scatter(x=x2, y=p2(x2), mode='lines', name='Catamarans Trendline',line=dict(color='#2e9db1', width=2)))
# 设置图表标题和轴标签
fig.update_layout(title='',xaxis_title='Year',yaxis_title='Listing Price',plot_bgcolor='white')

# 显示图表
fig.show()


