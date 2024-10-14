import datetime

today = datetime.datetime.now()
# 날짜,시간,밀리초
print(today)
# 날짜 포맷
now_date = today.strftime("%Y-%m-%d")
print(now_date)
print(type(now_date))
now_datetime = today.strftime("%Y-%m-%d %H:%M:%S")
print(now_datetime)