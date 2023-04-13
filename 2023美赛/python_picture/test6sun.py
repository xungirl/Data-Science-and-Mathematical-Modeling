import pandas as pd
import plotly.express as px

# 读取Excel文件
file_path = 'MS333.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')


# 假设你的数据有以下三列：id、parent和value
id_col = 'Make'
parent_col = 'Series'
value_col = 'count'

# 创建旭日图
fig = px.sunburst(df,path=[id_col, parent_col],values=value_col,color=id_col,color_discrete_sequence=['#ffd0ac',  '#b0b6fc','#f7a99c'],)
fig.update_traces(textinfo='label+percent parent')
# 设置图表标题
fig.update_layout(title='',   font=dict(
        family="Arial",  # 更改为所需字体，例如 "Courier New"、"Times New Roman" 等
        size=15,  # 更改字体大小
        color="black"  # 更改字体颜色
    ))

# 显示图表
fig.show()
