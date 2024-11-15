from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# # 파일 불러와서 저장하기 - 1회
# for i in range(2020,2024):
#   url = f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
#   browser = webdriver.Chrome()
#   # 이동하려는 주소 입력
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   # 파일 저장하기
#   with open(f'd1106/screen{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

with open('d1106/screen2023.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,'lxml')

# 기준점
data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc > ul")  
screens = data.select("li")
print(len(screens))

print("프로그램 종료")  


