import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%EC%97%90%EC%8A%A4%ED%8C%8C+%EC%B9%B4%EB%A6%AC%EB%82%98")
time.sleep(5)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')
i=1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'imgs_homework/{i}.jpg')
    i+=1

driver.quit()