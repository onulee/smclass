import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# html 전체를 가져옴.
soup = BeautifulSoup(res.text,"lxml")
cont = soup.find("div",{"class":"rankingnews_box_wrap _popularRanking"})
rankLists = cont.find_all("div",{"class":"rankingnews_box"})


# 파일 1줄씩 저장하시오.
with open("a.txt","w",encoding="utf-8") as f:
  print("개수확인 : ",len(rankLists))
  f.write(f"개수확인 : {len(rankLists)}\n")
  for idx,rankList in enumerate(rankLists):
    # 언론사 이름 출력
    print(f"[ {idx+1}. 언론사 : {rankList.find("strong",{"class":"rankingnews_name"}).text} ]")
    f.write(f"[ {idx+1}. 언론사 : {rankList.find("strong",{"class":"rankingnews_name"}).text} ]\n")
    news = rankList.find("ul",{"class":"rankingnews_list"})
    newsLists = news.find_all("li")
    # print("랭킹박스 안 뉴스 개수 : ",len(newsLists))
    for i,newsList in enumerate(newsLists):
      print(f"{i+1} : {newsList.find("a").text}")
      f.write(f"{i+1} : {newsList.find("a").text}\n")

print("완료")      