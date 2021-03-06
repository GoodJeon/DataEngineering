import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures


# 1. 데이터 준비
df = pd.read_csv('weight_height.csv', encoding='euc-kr')
# print(df)
# 학교명, 학년, 성별, 키, 몸무게 
df = df[['학교명','학년','성별','키','몸무게']]
# print(len(df))
df.dropna(inplace=True)
# print(len(df))


# df['학교명'] 초등학교 : 0 / 중학교 : 6  / 고등학교 : 9 + df[학년]
df['grade'] = list(map(lambda x: 0 if x[-4:] == '초등학교' else 6 if x[-3:] == '중학교' else 9, df['학교명'])) + df['학년']
# print(df)
df.drop(['학교명','학년'], axis='columns', inplace=True)
df.columns = ['gender', 'height', 'weight','grade']
# print(df)


# 남자 : 0 / 여자  : 1
# df['gender'] = list(map(lambda x: 0 if x == '남' else 1, df['gender']))
# df['gender'] = df['gender'].map(lambda x: 0 if x =='남' else 1)
df['gender'] = df['gender'].map({'남' : 0, '여' : 1})

# print(df)

is_boy = df['gender'] == 0
boy_df, girl_df = df[is_boy], df[~is_boy]

X = df[['weight','gender']]
y = df['height']

poly = PolynomialFeatures()
X = poly.fit(X).transform(X)



# 2. 데이터 분할
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.3, random_state=1)
# train_X = train_X.values.reshape(-1, 1)
# test_X = test_X.values.reshape(-1, 1)





# 3. 준비
# 하이퍼 파라미터 튜닝
linear = MLPRegressor(activation='relu', hidden_layer_sizes=(200, 2), solver='adam')




# 4. 학습
linear.fit(train_X, train_y)


# 5. 예측
predict = linear.predict(test_X)
print(predict)

# 평가
accuracy = linear.score(test_X, test_y)
print('acc:', accuracy)


# 그래프 그리기
# plt.plot(test_X, test_y, 'b.')
# plt.plot(test_X, predict, 'r.')



# plt.xlim(10, 140)
# plt.ylim(100, 220)

# plt.show()