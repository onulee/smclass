import os
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

# 순위, 사진링크주소, 제목,가수명
# 기준점
data = soup.select_one("#frm > div > table")
lists = data.select("tr")
print(len(lists))
print(lists[0])
title = []
# 타이틀 출력
tits = lists[0].select("th")
for tit in tits:
  title.append(tit.text.strip())
  print(tit.text.strip(),end="\t")
print()  

# 100위 출력
for i in range(1,11):
  if not os.path.exists("c1022/melon"):
    os.makedirs("c1022/melon")
   
  # 파일저장
  with open(f"c1022/melon/{i}.jpg","wb") as f:
    lis = lists[i].select("td")
    print(lis[1].select_one("span").text)
    print(lis[3].select_one("img")['src'])
    img = requests.get(lis[3].select_one("img")['src'])
    f.write(img.content)
    # 곡정보
    songs = lis[5].select("div.ellipsis")
    print(songs[0].select_one("span>a").text)
    print(songs[1].select_one("a").text)
    print("-"*30)

