import matplotlib.pyplot as plt

# 给定的x和y轴数据
x_data = [1, 2, 3]
y_data = [2.07, 0.347, 0.204]

# 将x轴数据转换为类别变量
x_data_categorical = ['1', '2', '3']
x_data_positions = [0, 0.5, 2]  # 自定义类别的位置

# 使用matplotlib绘制折线图
fig, ax = plt.subplots()
ax.plot(x_data_positions, y_data, marker='o', linestyle='-')

# 在折线图中标出点的位置
ax.scatter(x_data_positions, y_data, color='red')

""" # 显示点的坐标
for x, y in zip(x_data_positions, y_data):
    ax.text(x, y, f'({x}, {y})', fontsize=9, horizontalalignment='left', verticalalignment='bottom') """

# 设置图表的标题、x轴标签和y轴标签
plt.title('Scree Plot')
plt.xlabel('Factor number')
plt.ylabel('Eigenvalue')

# 自定义x轴刻度
ax.set_xticks(x_data_positions)
ax.set_xticklabels(x_data_categorical)


plt.yticks([0,0.5,1,1.5,2,2.5])
# 显示折线图
plt.show()
