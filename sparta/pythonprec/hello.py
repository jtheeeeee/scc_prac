import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
tr_tag= soup.select('#old_content > table > tbody > tr')
for tr in tr_tag:

    rank = tr.select_one('#old_content > table > tbody > tr > td:nth-child(1) >img ')

    title= tr.select_one('#old_content > table > tbody > tr > td.title > div > a')
    star = tr.select_one('#old_content > table > tbody > tr > td.point')
    if title is not None:
        doc = {'rank':rank['alt'], 'name' : title.text , 'star' :star.text}
        db.movies.insert_one(doc)