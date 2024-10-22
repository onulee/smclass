import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
data = soup.select_one("#contentarea > div.box_type_l > table")
stocks = data.select("tr")
# print("개수 : ",len(stocks))

# 파일 저장
f = open('c1022/stock.txt','w',encoding="utf-8")

# 상단타이틀 출력
tits = stocks[0].select("th")
title = []
for tit in tits:
  title.append(tit.text)
  print(tit.text,end="\t")
print()  
print("-"*80)

f.write(','.join(title)+"\n")

# 주식 30개 출력 - 5개 출력 / 출력과 동시에 리스트에 추가
st_lists = []
for i in range(2,50):
  st_list = []
  sts = stocks[i].select("td")
  if len(sts) <= 1: continue  # td가 1개 이하이면 제외
  for idx,st in enumerate(sts):
    s = ""
    if idx == 4:
      s = st.select_one("span").text
      s += st.select_one("span").next.next.next.text.strip()
      print(st.select_one("span").text,end="")
      print(st.select_one("span").next.next.next.text.strip(),end="\t")
    else:
      s = st.text.strip()
      print(st.text.strip(),end="\t")
    st_list.append(s)
  
  f.write(','.join(st_list)+"\n")  
  st_lists.append(st_list)
  print()
  print("-"*30)

f.close()
print("완료")

