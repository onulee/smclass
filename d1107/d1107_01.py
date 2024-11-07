from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

### request 라이브러리 가져오기
# url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
# res = requests.get(url,headers=headers)
# res.raise_for_status() # 에러시 종료


# selenium 라이브러리 가져오기
for i in range(2020,2024):
  url = f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
  browser = webdriver.Chrome()
  # 이동하려는 주소 입력
  browser.get(url)
  time.sleep(3)
  soup = BeautifulSoup(browser.page_source,"lxml")
  # 파일 저장하기
  with open(f'd1107/screen{i}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

print("프로그램 완료")