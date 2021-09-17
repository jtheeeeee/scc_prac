from pymongo import MongoClient
#내 컴퓨터에서 돌아가는 db를 사용할 것이다.
client = MongoClient('localhost', 27017)
#dbspart db를 사용할 것이다. 없다면 자동 생성
db = client.dbsparta

# insert
# doc = {'name':'jane','age':21}
# #db.user: 콜렉션
# db.users.insert_one(doc)


# find

same_ages = list(db.users.find({},{'_id':False}))
print(same_ages)
user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)
# update
db.users.update_one({'name':'bobby'},{'$set':{'age':100}})
# delete
db.users.delete_one({'name':'bobby'})


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})