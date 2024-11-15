# 다음 아이디, 패스워드 로그인
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random

# 1. 네이버항공권 페이지 열기
url = "https://flight.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화
browser.get(url)



prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이 :",prev_height)

# 스크롤 내리기 - 1000
while True:
  browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
  time.sleep(2) # 다른정보가 추가될때까지 대기
  # 높이 확인 - 2000
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if prev_height == curr_height:
    break
  prev_height = curr_height
  print("현재 높이 :",curr_height)