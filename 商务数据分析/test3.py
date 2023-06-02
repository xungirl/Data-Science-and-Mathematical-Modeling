import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

# 数据预处理
input_file = 'processed_videogame_sales.xlsx'
df = pd.read_excel(input_file, sheet_name='data')

# 选择特征和目标变量
X = df[['Platform', 'Genre', 'Publisher', 'Year']]
y = df['Global_Sales']

# 对分类特征进行独热编码
categorical_features = ['Platform', 'Genre', 'Publisher']
one_hot_encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
column_transformer = ColumnTransformer(transformers=[('cat', one_hot_encoder, categorical_features)], remainder='passthrough')
X_encoded = column_transformer.fit_transform(X)

# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 构建神经网络
input_shape = (X_train.shape[1],)
inputs = tf.keras.Input(shape=input_shape)
x = tf.keras.layers.Dense(128, activation='relu')(inputs)
x = tf.keras.layers.Dense(64, activation='relu')(x)
x = tf.keras.layers.Dense(32, activation='relu')(x)
outputs = tf.keras.layers.Dense(1, activation='linear')(x)

model = tf.keras.Model(inputs=inputs, outputs=outputs)

# 编译模型
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='mean_squared_error')

# 训练模型
model.fit(X_train, y_train, batch_size=32, epochs=100, validation_split=0.1, verbose=1)

# 评估模型
train_loss = model.evaluate(X_train, y_train)
test_loss = model.evaluate(X_test, y_test)
print(f"Train loss: {train_loss:.4f}")
print(f"Test loss: {test_loss:.4f}")