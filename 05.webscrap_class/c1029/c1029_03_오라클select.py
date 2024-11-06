import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
## sql창이 열림
cursor = conn.cursor()

# sql작성,실행
num = input("숫자를 입력하세요>>(,해서 입력하시오.) ")
# 10,20,30
n_list = num.split(",")
num2 = 20
# no=10,20,30 을 검색해서 출력하시오. 
# sql = "select * from students where no in(:no1,:no2,:no3)"
# cursor.execute(sql,no1=num,no2=num2,no3=num3)

# 3. excute함수 : 리스트 값 전달 
# excute뒤에는 dict,list,tuple타입만 가능
sql = "select * from students where no in(:1,:2)"
cursor.execute(sql,[num,num2])

# 2. excute함수 : 변수 key값 전달
# sql = "select * from students where no>:no"
# cursor.execute(sql,no=num)

# 1.문자열함수 f사용
# sql = f"select * from students where no>={num}"
# cursor.execute(sql)

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




