import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
import re

client = MongoClient('localhost', 27017)
db = client.dbsparta

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
tr_tag=soup.select('#body-content > div.newest-list > div > table > tbody > tr')
for tr in tr_tag:
    number = tr.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.number').text
    span =  tr.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.number > span')
    title = tr.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.title.ellipsis').text
    artist = tr.select_one('#body-content > div.newest-list > div > table > tbody > tr > td.info > a.artist.ellipsis').text
    if span is not None:
        number = number.replace(span.text,'')
    print(number.replace(span.text,'').replace('\n','').strip(),title.replace('\n','').strip(),artist.strip())
