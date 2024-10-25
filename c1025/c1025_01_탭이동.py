from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv

# 1.
# 네이버 쇼핑 검색창 입력 enter키 입력
url = "https://www.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
elem = browser.find_element(By.ID,"query")

# 네이버 쇼핑 클릭
elem = browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
elem.click()
time.sleep(2)

# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력
# 새로운 탭으로 이동
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]')
elem.send_keys("무선 마우스")
elem.send_keys(Keys.ENTER)

input("enter키 입력완료")

# 로딩 대기
# WebDriverWait(browser,5).until(lambda x:x.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]'))


soup = BeautifulSoup(browser.page_source,"lxml")
with open('c1025/naver.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())




2.
# 제목,금액,평점,평가수,찜 정보를 1-5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   print(url)


