import os
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# 1. 기준점.
data = soup.select_one("#frm > div > table")
# 101개
lists = data.select("tr")

# lists[0] : 상단타이틀
title = []
tits = lists[0].select("th")
for tit in tits:
  title.append(tit.text.strip())
  # print(tit.text.strip())

# 1-100위 리스트 출력
for i in range(1,101):
  # 폴더가 존재하지 않으면
  if not os.path.exists("c1022/melon"):
    os.makedirs("c1022/melon")
      
  with open(f"c1022/melon/{i}.jpg","wb") as f:
    lis = lists[i].select("td")
    print("순위 :",lis[1].select_one("span").text)
    print("이미지 :",lis[3].select_one("img")['src'])
    img = requests.get(lis[3].select_one("img")['src'])
    f.write(img.content)
    songs = lis[5].select("div.ellipsis")
    print("곡정보 :",songs[0].select_one("a").text,end="")
    singers = songs[1].select("a")
    if len(singers) != 4:
      print(singers[0].text)
    else:
      print(singers[0].text+"-"+singers[1].text)  
    print("-"*50)
  
