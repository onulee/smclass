import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)

# html 전체를 가져옴.
soup = BeautifulSoup(res.text,"lxml")
# 기준점
data = soup.select_one("#wrap > div.rankingnews._popularWelBase._persist > div.rankingnews_box_wrap._popularRanking > div")
ranks = data.select("div.rankingnews_box")
title = ranks[0].select_one("strong.rankingnews_name").text
print(title)
f = open("news.txt","w",encoding='utf-8')
f.write(title+"\n")
r_lists = ranks[0].select("ul.rankingnews_list>li")
for i,r_list in enumerate(r_lists):
  no = f"{i+1}"
  print(no)
  rnews = r_list.select_one("div.list_content>a").text
  print(rnews)
  f.write(f"{no},{rnews}\n")
  
f.close()  




