import requests
from bs4 import BeautifulSoup
import pandas as pd
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
data = soup.select_one("div#contentarea")
type1 = data.select_one("tr.type1")
th_datas = type1.select("th")

th_list = []
for th_data in th_datas:
    th_list.append(th_data.text)
    print(th_data.text)
dic = {"증권제목":th_list} 
df = pd.DataFrame(dic)
df.to_csv("data.csv",encoding="utf-8",index=False)   
