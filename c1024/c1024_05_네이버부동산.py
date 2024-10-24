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
import pyautogui

# url = "https://new.land.naver.com/complexes?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"


# browser = webdriver.Chrome()
# browser.maximize_window()
# browser.get(url)

# pyautogui.moveTo(1270,550)
# time.sleep(1)
# pyautogui.moveTo(1270,480)
# pyautogui.click()
# time.sleep(1)
# pyautogui.moveTo(200,800)
# time.sleep(1)
# prev_height = browser.execute_script("return articleListArea.scrollHeight")
# print("화면 높이 : ",prev_height)
# while True:
#   # browser.execute_script("window.scroll(0,articleListArea.scrollHeight)")
#   pyautogui.scroll(-prev_height)
#   time.sleep(2)
#   curr_height = browser.execute_script("return articleListArea.scrollHeight")
#   if prev_height == curr_height: break
#   prev_height = curr_height
#   print("높이 : ",prev_height)

# # print("-"*50)
# # all_height = browser.execute_script("return document.body.scrollHeight")
# # print("화면 전체 높이 : ",all_height)

# # 파일저장
# # soup = BeautifulSoup(browser.page_source,"lxml")
# # data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div")
# # with open("c1024/naver.html","w",encoding="utf-8") as f:
# #   f.write(soup.prettify())
# input("엔터키 입력완료")

# 숫자로 변경하는 방법 - 10억5,000  - 10 , 5,000  ''
def price_chg(p):
  b = p.split('억')
  f_num = int(b[0])*100000000
  if b[1].strip() != '':
    s_num = int(b[1].strip().replace(",",""))*10000
  else:
    s_num = 0  
  price = f_num+s_num
  return price

# 138/101m², 7/35층, 남향
def spec_chg(spec):
  spec_a = spec.split(",")
  spec_b = spec_a[0].split("/")
  spec_c = int(spec_b[1][:-2])
  return spec_c

# 84타입, 59
# 매매가격이 낮은 5개, 전세가격이 낮은 5개를 출력하시오.
with open("c1024/naver.html","r",encoding="utf-8") as f:
  soup = BeautifulSoup(f,"lxml")
# 기준점  
data = soup.select_one("#articleListArea")
# 리스트형태를 가져오기
areas = data.select("div.item")

# 분류별 가져오기
print(f"[ 총개수 : {len(areas)} ]")
print("-"*50)

house_list = []

for idx,area in enumerate(areas):
  print(f"{idx+1}.")
  # 분류 : 매매,전세 월세-제외
  type = area.select_one("div.price_line>.type").text.strip()
  if type == '월세': 
    print("월세 제외")
    continue
  print("분류 :",type)
  # 가격 - 문자열
  price = area.select_one("div.price_line>.price").text.strip()
  # 숫자변환 함수를 생성호출
  price = price_chg(price)
  print(f"금액 :{price:,}")
  # 138/101m², 7/35층, 남향
  spec = area.select_one("div.info_area > p:nth-child(1) > span").text.strip()
  # spec분리 함수를 생성호출 - int
  spec = spec_chg(spec)
  print("타입 :",spec)
  print("-"*50)

  # list저장
  house_list.append([type,price,spec])


print("[ 리스트 출력 ]")

# 매매리스트 생성 - 평수별로 구분
h1_list = [x for x in house_list if x[0]=='매매']
# 전세리스트 생성
h2_list = [x for x in house_list if x[0] == '전세']

# 매매순차정렬
h1_list.sort(key=lambda x:x[1])
print(h1_list[:5])

# 전세순차정렬
h2_list.sort(key=lambda x:x[1])
print(h2_list[:5])

