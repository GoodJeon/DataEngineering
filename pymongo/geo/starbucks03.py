'''
1. starbucks_all.json을 읽어온다.
2. 읽어온 파일 한 줄 씩 json_data로 저장한다.
3. json_data를 dictionary로 변환한다.(result_dict)
 result_dict에 'list'라는 키를 입력하여, 리턴된 value를 반복문으로 출력하자.
'''


import json


with open('starbucks_all.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

result_dict = dict(json_data)

for data in result_dict['list']:
    print(data)


# 4. mongodb와 연결(db: test / collection : starbucks01)
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.test
starbucks01 = db.starbucks01


# 5. result_dict['list'] 값을 mongodb에 저장
# result = starbucks01.insert_many(result_dict['list'])
# print(result)

# 6. starbucks01 collection 전체 출력
all = starbucks01.find({},{'_id':False})
for data in all:
    print(data)