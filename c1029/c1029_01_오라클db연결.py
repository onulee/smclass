import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
## sql창이 열림
cursor = conn.cursor()

# sql작성,실행
num = input("숫자를 입력하세요.>> ")
sql = "select * from students"
cursor.execute(sql)

# 데이터 가져오기 - fetchone():1개,fetchmany(10):숫자만큼,fetchall():모든것
rows = cursor.fetchall()
titles = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']
for title in titles:
  print(title,end="\t")
print()
print("-"*80)  

for row in rows:
  for i,r in enumerate(row):
    if i == 1:
      print(f"{r:10s}",end="\t")
      continue
    if i == 6:
      print(f"{r:.2f}",end="\t")
      continue
    if i == 8:
      # strftime()함수 : 날짜포맷함수 %Y : 2024 , %y : 24
      print(r.strftime("%Y-%m-%d"),end="\t")
      continue
    print(r,end="\t")
  print()  
  
# 종료
conn.close()  




