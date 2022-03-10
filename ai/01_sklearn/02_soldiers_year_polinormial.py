# pip install pandas
import pandas as pd
from sklearn.model_selection import train_test_split    
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
import numpy as np


# 1. 데이터 준비
# df = pd.read_csv('soldiers.csv', encoding='euc-kr')
# print(df)
names = ['순번', 'date', '가슴둘레', '소매길이', 'height', '허리둘레', '살높이', '머리둘레', '발길이', 'weight']
df = pd.read_csv('soldiers.csv', encoding='euc-kr', names=names, header=0, low_memory=False)
# print(df)
df = df[['date','height','weight']]
# print(df)
print(len(df))

# inplace=True는 df에 dropna가 적용된 것을 원본으로 바꿔버릴 때 사용
df.dropna(inplace=True)
print(len(df))

# 년도만 남기자
df['date'] = list(map(lambda x: int(str(x)[:4]) if len(str(x)) > 4 else x , df['date']))
# print(df)
# 2013 : 0 / 2014: 1 / ... 2017 : 4
df['date_new'] = list(map(lambda x: 0 if x == 2013 else 1 if x == 2014 else 2 if x == 2015 else 3 if x == 2016 else 4, df['date'])) 



# 키를 float으로 바꾸자(cm도 제거)
df['height'] = list(map(lambda x: float(str(x)[:5]) if len(str(x)) > 5 else x , df['height'] ))
# print(df)


# 몸무게를 float으로 바꾸자(kg도 제거)
df['weight'] = list(map(lambda x: str(x).split(' ')[0], df['weight']))
df['weight'] = list(map(lambda x: float(x) if x else None, df['weight']))
df.dropna(inplace=True)
# print(df)
# print(len(df))


X = df[['weight', 'date_new']]
y = df['height']

# 다항회귀 (PolynormialFeatures) : 특성이 두 개. 특성을 곱해서 다차원으로 바꾸자.
# [1, a, b, a^2, ab, b^2]
poly = PolynomialFeatures()
X = poly.fit(X).transform(X)




# 2. 데이터 분할
# train_x, test_x

# random_state는 randomseed같은 것
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)
# print(train_x)
# print(train_y)

# train_X = train_X.values.reshape(-1,1)
# test_X = test_X.values.reshape(-1,1)
# print(train_X)




# 3. 준비
linear = LinearRegression()



# 4. 학습
linear.fit(train_X, train_y)



# 5. 예측
predict = linear.predict(test_X)
# print(test_X)
# print(predict)

print(linear.predict(poly.fit(np.array([[70,0]])).transform(np.array([[70,0]]))))

plt.plot(test_X, test_y, 'b.')
plt.plot(test_X, predict, 'r.')

plt.xlim(20, 150)
plt.ylim(150, 220)
plt.grid()


plt.show()
