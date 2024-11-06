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

# 제목,금액,평점,평가수,찜 정보를 1-5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

# # # 파일저장하기
# browser = webdriver.Chrome()
# browser.maximize_window()
# for i in range(1,6):
#   url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
#   browser.get(url)
#   time.sleep(2)
  
#   # # 화면을 스크롤해서 내리기 반복
#   prev_height = browser.execute_script("return document.body.scrollHeight")

#   while True:
#     browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#     time.sleep(1)
#     # 페이지가 로딩되면서 길어진 길이를 다시 가져옴.
#     curr_height = browser.execute_script("return document.body.scrollHeight")
#     # 페이지를 스크롤해서 길이가 더 길어졌는지 확인
#     if prev_height == curr_height:
#       break
#     # 더 길이가 길어졌으면, 이전길이에 현재길이를 입력시킴
#     prev_height = curr_height
#   print("스크롤 내리기 완료")  
  
#   soup = BeautifulSoup(browser.page_source,"lxml")
#   with open(f'c1025/navershop{i}.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())
#   time.sleep(2)
# input("enter키 입력완료")


# 파일 불러오기
with open(f'c1025/navershop1.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,"lxml")

data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx>div")

# 클래스 종류 2개 : adProduct_item__1zC9h , product_item__MDtDF
# pros = data.select("div.adProduct_item__1zC9h")+data.select("div.product_item__MDtDF")
# pros = data.select("div.adProduct_item__1zC9h")
pros = data.select(".product_item__MDtDF")
print(len(pros))

# for idx,pro in enumerate(pros):
#   print(idx,".")
#   if pro['class'][0] == 'adProduct_item__1zC9h':
#    pass
#   else:
#     pass

# class : product_item__MDtDF 상품
title = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_title__Mmw2K > a").text.strip()
print(title)
price = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text.strip().replace(",","")
print(price)
rating = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:]
print(float(rating))
p_count = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > em").text.strip().replace("\n","").replace(" ","")[1:-2]
print(float(p_count)*10000)
a_count = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > span:nth-child(2) > span").text.strip().replace(",","")
print(int(a_count))

# class : adProduct_item__1zC9h 상품
# title = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a").text.strip()
# print(title)
# price = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_price_area__yA7Ad > strong > span.price > span > em").text.strip().replace(",","")
# print(price)
# rating = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > span.adProduct_rating__PaMzh").text.strip()
# print(float(rating))
# p_count = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_etc_box__UJJ90 > span:nth-child(1) > a > em").text.strip()
# print(int(p_count))
# a_count = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_etc_box__UJJ90 > span:nth-child(2) > span").text.strip()
# print(int(a_count))







# 1.상단타이틀. csv파일로 저장
# f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)
# st_list = [ st.text  for st in stocks[0].select("th") ]
# writer.writerow(st_list)






