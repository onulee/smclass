# 다음 아이디, 패스워드 로그인
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
import random
url = "https://www.daum.net/"

# 크롬브라우저 열기
browser = webdriver.Chrome()
# 네이버페이지 이동
browser.get(url)
time.sleep(3)
# 로그인버튼 선택
elem = browser.find_element(By.XPATH,'//*[@id="loginMy"]/div/div[1]/div/a')
# 로그인버튼 클릭
elem.click()
time.sleep(random.randint(2,5))

# 자동화 방지를 위한 자바스크립트 활용 데이터 입력
input_js = 'document.getElementById("loginId--1").value="{id}"; \
            document.getElementById("password--2").value="{pw}"; \
           '.format(id="onulee74",pw="1")
time.sleep(random.randint(2,5))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

time.sleep(random.randint(2,5))
elem = browser.find_element(By.XPATH,'//*[@id="mainContent"]/div/div[1]/form/div[4]/button[1]')
time.sleep(random.randint(2,5))
# 로그인 버튼 클릭
elem.click()


#완료
time.sleep(100)


