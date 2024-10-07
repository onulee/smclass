students = []
no = 1
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수

import datetime
today = datetime.datetime.now()
date = "{:%y-%m-%d}".format(today)
print(date)
time = "{:%H:%M:%S}".format(today)
print(time)
print(today.year)
print(today)


# 학생성적프로그램
while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    pass
  elif choice =="2":
    pass
  elif choice =="3":
    pass
  elif choice =="4":
    pass
  elif choice =="0":
    pass


