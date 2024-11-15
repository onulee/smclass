import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"class":"rankingnews_box_wrap"}))
newList = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
print(1,"="*20)
print(newList)
print(1,"="*20)

# next : 검색태그 다음뒤에 오는 태그를 찾아줌
# next_sibling : 검색태그의 형제관계의 다음태그를 찾아줌.
print(newList.next_sibling.next_sibling)


print("여러개 개수 확인 : ",len(newList))