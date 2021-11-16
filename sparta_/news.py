from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook

driver = webdriver.Chrome('chromedriver')

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles= soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사"])
for article in articles:
    title = article.select_one('div.news_area > a')
    url=title['href']
    comp = article.select_one('div.info_group > a')
    ws1.append([title.text, url, comp.text.replace("언론사 선정","")])

driver.quit()
wb.save(filename='articles.xlsx')
