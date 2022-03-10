from pymongo import MongoClient


client = MongoClient('mongodb://localhost:27017')
db = client['test']
score = db['score']

# 이름이 유재석인 doc 찾아서 midterm의 kor 점수를 100점으로 변경하자!
# doc 하나만 변경

result01 = score.update_one({'name':'유재석'}, {'$set':{'kor':100}})

# print(result01.matched_count)
# print(result01.modified_count)


result02 = score.update_many(
    {'eng':{'$gt':80}},
    {'$set': {'eng': 0}}
)
print(result02.matched_count)
print(result02.modified_count)