from bs4 import BeautifulSoup
from selenium import webdriver
from openpyxl import Workbook
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

driver = webdriver.Chrome('chromedriver')


wb = Workbook()
ws1 = wb.active
ws1.title = "articles"
ws1.append(["제목", "링크", "신문사", "썸네일"])

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EC%B6%94%EC%84%9D"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles= soup.select('#main_pack > section.sc_new.sp_nnews._prs_nws > div > div.group_news > ul > li')
for article in articles:
    title = article.select_one('div.news_area > a')
    url=title['href']
    comp = article.select_one('div.info_group > a')
    thumbnail= article.select_one("a > img")['src']
    ws1.append([title.text, url, comp.text.replace("언론사 선정",""), thumbnail])

wb.save(filename='articles.xlsx')
driver.quit()


# 보내는 사람 정보
me = "jth970317@gmail.com"
my_password = "0317*HTJ"

# 로그인하기
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login(me, my_password)

# 받는 사람 정보
emails = ['j_03_17@naver.com','j_03_17@naver.com']

for you in emails:
# you = "j_03_17@naver.com"

    # 메일 기본 정보 설정
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "이것이 제목이다."
    msg['From'] = me
    msg['To'] = you

    # 메일 내용 쓰기
    content = "추석 기사란다."
    part2 = MIMEText(content, 'plain')
    msg.attach(part2)
    part = MIMEBase('application', "octet-stream")
    with open("articles.xlsx", 'rb') as file:
        part.set_payload(file.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment", filename="추석기사.xlsx")
    msg.attach(part)

    # 메일 보내고 서버 끄기
    s.sendmail(me, you, msg.as_string())

s.quit()