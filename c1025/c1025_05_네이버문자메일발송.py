from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv
# email 발송관련
import smtplib
from email.mime.text import MIMEText

smtpName = "smtp.naver.com"
smtpPort = 587

# 자신의 네이버메일주소,pw, 받는사람이메일주소
sendEmail = "onulee@naver.com"
pw = "1111***"
recvEmail = "onulee@naver.com"

title = "제목 : 파이썬 이메일보내기 안내"
content = """\
파이썬에서 text 이메일을 보냅니다.
여러줄 쓰기 형태로 보냅니다.
네이버 smtp서버를 사용해서 보냅니다.
"""

# 설정
msg = MIMEText(content)
msg['Subject'] = title
msg["From"] = sendEmail
msg['To'] = recvEmail
print("msg 데이터 : ",msg.as_string())

# 서버이름,서버포트
s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()
# 2단계 보안설정이 되어 있는 경우는 에러 발생
# 인증키 발급을 받아야 함.
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
s.quit()

# 메일발송 완료
print("메일을 발송했습니다.")