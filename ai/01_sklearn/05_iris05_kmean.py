from random import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

import pandas as pd
import matplotlib.pyplot as plt

# 1
iris = load_iris()
X = iris.data
y = iris.target

# 2
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.3,random_state=1)


# 3
# 분류하고자 하는 갯수가 3개이기 때문에(setosa, vergi~, verginica)
model = KMeans(n_clusters=3)


# 4
# 중심을 알아서 찾기 때문에(비지도 학습 군집) 문제만 넣고 답을 넣어주지 않아도 데이터를 알아서 넣어줄 것이다.
model.fit(train_X)


# 5
pred = model.predict(test_X)
print(test_X)
print(pred)


# 어떻게 군집한건지 그림 그리기
df = pd.DataFrame(test_X)
df.columns = ['sepal_length','sepal_width','petal_length','petal_width']
df['category'] = pd.DataFrame(pred)


centers = pd.DataFrame(model.cluster_centers_)
centers.columns = ['sepal_length','sepal_width','petal_length','petal_width']
center_X = centers['sepal_length']
center_y = centers['sepal_width']

plt.scatter(df['sepal_length'], df['sepal_width'], c=df['category'])
plt.scatter(center_X, center_y, s=100, c='r', marker='*')
plt.show()