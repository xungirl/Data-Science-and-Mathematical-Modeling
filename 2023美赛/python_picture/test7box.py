import pandas as pd
import plotly.graph_objects as go

# 读取Excel文件
excel_file = 'box.xlsx'
df = pd.read_excel(excel_file,sheet_name='MS-Jeaneau', engine='openpyxl')

# 对数据进行分组，根据ShipType
grouped_data = df.groupby('Series')

# 创建箱线图
fig = go.Figure()

# 为每个船种类添加一个箱线图
for ship_type, group_data in grouped_data:
    fig.add_trace(go.Box(y=group_data['Listing Price'], name=ship_type, boxpoints='all', jitter=0.3, pointpos=-1.8))

# 设置图表标题和坐标轴标题
fig.update_layout(title='', xaxis_title='Series', yaxis_title='Listing Price',plot_bgcolor='white',font=dict(size=16),title_font=dict(size=24))

# 显示箱线图
fig.show()
