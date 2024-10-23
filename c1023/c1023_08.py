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

# 2. 출발지 - 입력,김포
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b').click()
time.sleep(1)
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("김포")
time.sleep(1)
# 화면창이 뜨기도 전에 선택이 되면 에러
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b').click()


# 3. 도착지 - 입력,제주
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]/b').click()
time.sleep(1)
browser.find_element(By.CLASS_NAME,"autocomplete_input__qbYlb").send_keys("제주")
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b').click()

# 4. 가는날 - 날짜선택 
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button/b').click()
# 5. 오는날 - 날짜선택
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button/b').click()

# 6. 인원 - 1명 추가
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]').click()
time.sleep(1)

# 7. 항공권검색 버튼 클릭
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]').click()
time.sleep(1)


# 8. 데이터를 검색하는 동안 대기 상태
# 검색중 
# time.sleep(7)
#--------------------
# 화면 대기 함수
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 화면대기 - 30초동안 대기
# 화면에 찾을려고 하는 <html>요소가 있는지 확인
elem = WebDriverWait(browser, 30).until(lambda x: x.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]'))
print(elem)
# 화면 스크롤 내리기
# 현재 스크롤 높이 검색 - 1000
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


# 데이터 가져와서 처리
# BeautifulSoup 데이터 처리
# 웹스크래핑
soup = BeautifulSoup(browser.page_source,"lxml")
with open('flight.html','w',encoding='utf-8') as f:
  f.write(soup.prettify())

input("enter키를 입력하면 프로그램이 종료됩니다.")
browser.quit()  

# 완료
time.sleep(100)


# # 페이지 열기
# browser = webdriver.Chrome()
# browser.get(url)
# elem = browser.find_element(By.ID,"query")
# elem.send_keys("네이버 항공권")
# elem.send_keys(Keys.ENTER)
# browser.find_element(By.CLASS_NAME,"link_name").click()



