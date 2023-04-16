from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# 定义KMeans，以及K值
kmeans = KMeans(n_clusters=n_clusters)	
# 根据数据data进行聚类，结果存放于result_list中
result_list = kmeans.fit_predict(data)
# 将原始的数据data和聚类结果result_list
# 传入对应的函数计算出该结果下的轮廓系数
score = silhouette_score(data, result_list)
