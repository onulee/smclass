from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random

# url = "https://www.yanolja.com/"
# # 브라우저 열기
# browser = webdriver.Chrome()
# # 창 최대화
# browser.maximize_window()
# # url입력
# browser.get(url)

# # 검색창 클릭
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()
# time.sleep(2)

# # 날짜선택
# browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()
# time.sleep(2)
# # 입실날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[2]').click()
# time.sleep(2)
# # 퇴실날짜
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()
# time.sleep(2)

# # 확인버튼 클릭
# browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()
# time.sleep(2)


# # 글자입력창 선택
# elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')
# elem.click()
# time.sleep(2)
# # 글자입력, enter키 입력
# elem.send_keys("강릉 호텔")
# time.sleep(2)
# elem.send_keys(Keys.ENTER)

# # 자동시 로딩 대기
# # 화면의 호텔검색내용이 뜰때까지 대기, 최대30초까지 대기
# WebDriverWait(browser,30).until(lambda x:x.find_element(By.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

# # 화면을 스크롤해서 내리기 반복
# # excute_script() : 자바스크립트 실행함수
# prev_height = browser.execute_script("return document.body.scrollHeight")

# while True:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)
#   # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#   if prev_height == curr_height:
#     break
#   # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#   prev_height = curr_height

# print("스크롤 내리기 완료")  

# soup = BeautifulSoup(browser.page_source,"lxml")
# # html저장하기
# with open('c1024/yanolja.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())
# input("Enter키를 입력하면 완료됩니다.")



# 파일불러와서 soup으로 파싱
with open('c1024/yanolja.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")

# 기준점
data = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
# 호텔 여러개 정보리스트
lists = data.select("div.PlaceListItemText_container__fUIgA")
print("개수 : ",len(lists))

true_num = 0 # 맞는 개수
fail_num = 0 # 맞지 않는 개수
except_num = 0 # 예외처리 - 마감(금액없을시)
search_list = []

for idx,list in enumerate(lists):
  try:
    rating = float(list.select_one("span.PlaceListScore_rating__3Glxf").text.strip())
    price = int(list.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK").text.strip().replace(",",""))
    if rating<4.8 or price>180000: 
      print(f"{idx+1}. 조건에 맞지 않음.")
      fail_num += 1
      continue
    print(f"{idx+1}.")
    name = list.select_one("strong.PlaceListTitle_text__2511B").text.strip()
    print("호텔명 :",name)
    print("평점 :",rating)
    print("금액 :",price)
    print("-"*50)
    search_list.append([idx+1,name,rating,price])
    true_num += 1
  except Exception as e:
    print(f"{idx+1}. 예외처리",e)
    except_num += 1

print("-"*50)
print("[ 검색 정보 ]")
print("-"*50)
print("1. 조건 맞는 개수 :",true_num)
print("2. 조건에 맞지 않는 개수 :",fail_num)
print("3. 예외처리 개수 :",except_num)

# 리스트에 담고 정렬
# print(search_list)
# [1,호텔명,평점,가격]
# 평점 역순정렬
search_list.sort(key=lambda x:x[2],reverse=True)
print(search_list[:5])

# 금액 순차정렬
search_list.sort(key=lambda x:x[3])
print(search_list[:5])



# # 평점이 4.8이상, 금액:17만원 이하 검색해서 출력하시오.
# # 1. 
# # 호텔명 : 
# # 평점 :
# # 금액 :
# # ----------------

# # [ 검색 정보 ]
# # 조건 맞는 개수 : 
# # 조건에 맞지 않는 개수 : 
# # 예외처리 개수 : 


