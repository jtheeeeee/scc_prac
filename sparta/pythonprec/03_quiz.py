from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

movie_star = db.movies.find_one({'name':'매트릭스'},{'_id':False})['star']
movie_titles= list(db.movies.find({'star':movie_star},{'_id':False}))
for title in movie_titles:
    print(title['name'])

db.movies.update_one({'name':'매트릭스'},{'$set':{'star':'0'}})
