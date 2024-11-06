import requests
from bs4 import BeautifulSoup
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

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

# 메일보내기
smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,pw, 받는사람이메일주소
sendEmail = "onulee@naver.com"
pw = "LDN53XPJ58R9"
recvEmail = "onulee@naver.com"

title = "랭킹뉴스"
content = "랭킹뉴스 파일을 첨부합니다."

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail
msg.attach(MIMEText(content))

# 파일첨부
with open("news.txt",'rb') as f:
  attachment = MIMEApplication(f.read()) # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename="news.txt")
  msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls() # 보안인증
# 2단계 보안설정이 되어 있는 경우는 에러 발생
# 인증키 발급을 받아야 함.
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string()) 
print("msg : ")
print(msg.as_string())
s.quit()

print("메일이 발송되었습니다.!")



