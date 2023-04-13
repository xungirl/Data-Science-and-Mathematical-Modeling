% 导入数据
data = readmatrix("data.xlsx");
data = array2table(data);  % 将矩阵转换为表格，以便后续处理
data = fillmissing(data, 'constant', mean(data{:,:}, 'omitnan')); % 用平均值替换缺失值

% 划分特征和目标变量
X = data(:, 1:9);
y = data(:, 10);

% 划分训练集和测试集
cv = cvpartition(height(data), 'HoldOut', 0.2);
idx = cv.test;
X_train = X(~idx, :);
X_test = X(idx, :);
y_train = y(~idx, :);
y_test = y(idx, :);

% 标准化数据
[X_train, mu, sigma] = zscore(X_train{:,:});
X_test = (X_test{:,:} - mu) ./ sigma;

% 构建神经网络
inputSize = 9;
hiddenLayerSize = [32, 16];
net = feedforwardnet(hiddenLayerSize);
net.layers{1}.transferFcn = 'tansig';
net.layers{2}.transferFcn = 'tansig';
net.layers{3}.transferFcn = 'purelin';
net.trainFcn = 'trainscg';
net.divideFcn = 'dividetrain';
net.performFcn = 'mse';

% 训练神经网络
[net, tr] = train(net, X_train', y_train{:,:}');

% 预测并计算R方
y_pred = net(X_test');
y_pred = y_pred';
r2 = 1 - sum((y_test{:,:} - y_pred).^2) / sum((y_test{:,:} - mean(y_test{:,:})).^2);
disp(['R-squared (R2): ' num2str(r2)]);
