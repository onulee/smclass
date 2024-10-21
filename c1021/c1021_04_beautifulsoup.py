import requests 
from bs4 import BeautifulSoup 

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()

with open("c1021/1.html","w",encoding="utf-8") as f:
  f.write(res.text)

# html,css 정보를 가진 소스변경
soup = BeautifulSoup(res.text,"lxml") # str -> html태그,css태그 사용될수 있는 형태로 변경

# BeautifulSoup 사용
# 태그 출력, 태그 글자 출력
print(soup.title)             # title태그 출력
print(soup.title.text)        # title태그 문자열을 출력 - text, get_text()
print("없는 태그 : ",soup.titletitle) # 없는 태그입력시 None
# print("없는 태그 : ",soup.titletitle.text) # 없을시 에러발생
print(soup.a)           # a태그 첫번째 것을 가져옴.
print(soup.a.next.text) #next 다음태그를 가져옴.
# 태그 속성  출력
print(soup.a.attrs)    # 태그의 속성값 가져옴 : 딕셔너리 형태
print(soup.a["href"])  # a태그의 href속성값을 가져옴.

# 특정정보를 출력
# print(soup.find("div",attrs={"id":"header"}))
print(soup.find("div",{"id":"header"}))   # div태그 id="header"
print(soup.find("h2",{"class":"rankingnews_tit"}).text) # h2태그 class="rankingnews_tit"의 text를 출력
print(soup.find_all("div"))   # 모든 div태그 검색
print(len(soup.find_all("div"))) # 모든 div태그 개수 출력
print(type(soup.find_all("div")))


# soup.prettify() 정보 저장
# with open("c1021/2.html","w",encoding="utf8") as f:
#   # soup.prettify() : 소스가 정리되어 저장됨.
#   f.write(soup.prettify())  

print("완료")


