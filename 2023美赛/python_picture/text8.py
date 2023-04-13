import pandas as pd
import plotly.express as px

# 读取Excel文件
excel_file = 'lengthandcount\jeaneau.xlsx'  # 请将此处的文件名替换为你的Excel文件名
#sheet_name = 'Sheet1'  # 请将此处的工作表名替换为你的Excel文件中的工作表名

# 使用pandas读取Excel文件并将其加载到数据框中
df = pd.read_excel(excel_file,  engine='openpyxl')

# 生成条形统计图
# 假设你的数据框有两列，分别是'Category'和'Value'，请根据你的实际数据调整这些列名
fig = px.bar(df, x='Length', y='count')

# 显示条形统计图
fig.show()
