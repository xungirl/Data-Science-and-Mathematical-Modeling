#from sklearn.metrics import calinski_harabaz_score
from sklearn.cluster import DBSCAN
for i in range(2,10):#k从2到10，逐个输出
    #构建并训练模型
    dbscan = DBSCAN(n_clusters = i,random_state=123).fit(data)
    score = calinski_harabaz_score(data,dbscan.labels_)
    print('数据聚%d类calinski_harabaz指数为:%f'%(i,score))



