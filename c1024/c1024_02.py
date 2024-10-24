from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

# 노트북 검색 된 사이트 1,2,3페이지 에서
# 만족도 95 이상이면서, 평가수 100이상, 금액 1500000이하 검색하시오.
# 화면에는 보이지 않지만 내부적으로 화면 크기 설정
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")

for i in range(3):
  url = f"https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p={i+1}"
  # 브라우저 열기
  browser = webdriver.Chrome(options=options)
  # 창 최대화
  browser.maximize_window()
  # url입력
  browser.get(url)
  time.sleep(3)
  soup = BeautifulSoup(browser.page_source,"lxml")
  # html저장하기
  with open(f'c1024/gmarket{i+1}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
  # 화면에는 보이지 않지만 스크린 샷 찍어서 저장
  

browser.get_screenshot_as_file("play.png")
input("Enter키를 입력하면 완료됩니다.")
