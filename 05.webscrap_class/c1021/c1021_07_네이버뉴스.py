import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
# print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newLists = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})

# 12번 반복
print("개수 : ",len(newLists))

# 여러개 출력
for idx,newList in enumerate(newLists):
  print(f"{idx+1}. 타이틀 :",newList.find("strong",{"class":"rankingnews_name"}).text)
  ranks = newList.find("ul",{"class":"rankingnews_list"})
  tlists = ranks.find_all("li")
  # 5번 반복
  for i,t in enumerate(tlists):
    print(i+1,":",t.find("a").text)



