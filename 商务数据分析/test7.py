import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf

# 读取数据
data = pd.read_excel('data.xlsx')

# 数据预处理
data.dropna(inplace=True)

# 对非数值列进行编码
encoder = LabelEncoder()
data['Platform'] = encoder.fit_transform(data['Platform'])
data['Genre'] = encoder.fit_transform(data['Genre'])
data['Publisher'] = encoder.fit_transform(data['Publisher'])

# 选择特征和目标变量
features = ['Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
target = 'Global_Sales'

X = data[features]
y = data[target]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 特征缩放
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 定义神经网络模型
class NeuralNetwork(tf.Module):
    def __init__(self, input_shape, layer_sizes):
        super(NeuralNetwork, self).__init__()
        self.layers = []
        for size in layer_sizes:
            self.layers.append(tf.keras.layers.Dense(size, activation='relu'))
        self.output_layer = tf.keras.layers.Dense(1)

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        x = self.output_layer(x)
        return x

# 创建神经网络实例
layer_sizes = [64, 32]
model = NeuralNetwork(len(features), layer_sizes)

# 定义损失函数和优化器
loss_fn = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam()

# 训练神经网络
epochs = 100
batch_size = 32
for epoch in range(epochs):
    for i in range(0, len(X_train), batch_size):
        X_batch = X_train[i:i+batch_size]
        y_batch = y_train[i:i+batch_size]

        with tf.GradientTape() as tape:
            y_pred = model(X_batch)
            loss = loss_fn(y_batch, y_pred)

        gradients = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(gradients, model.trainable_variables))

    print(f"Epoch {epoch+1}, Loss: {loss.numpy()}")

# 评估模型性能
y_pred = model(X_test)
test_loss = loss_fn(y_test, y_pred)
print(f"Test loss: {test_loss.numpy()}")