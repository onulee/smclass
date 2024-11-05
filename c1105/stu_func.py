import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

### db연결 함수선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외처리 : ",e)
  return conn

### 0. 메인화면출력함수 선언
def main_print():
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("4. 학생성적정렬")   # 이름순차정렬,이름역순정렬,합계순차정렬,합계역순정렬
  print("5. 등수처리")
  print("0. 프로그램종료")
  choice = input("원하는 번호를 입력하세요.>> ")
  return choice


### 1. 학생성적입력함수 선언
def stu_insert():
  conn = connects()
  cursor = conn.cursor()
  print("[ 학생성적 입력 ]")
  name = input("학생이름을 입력하세요.>> ")
  kor = int(input("국어점수를 입력하세요.>> "))
  eng = int(input("영어점수를 입력하세요.>> "))
  math = int(input("수학점수를 입력하세요.>> "))
  total = kor+eng+math
  avg = total/3
  # list
  s_list = [name,kor,eng,math,total,avg]
  # insert,update,delete 경우 conn.commit() 하셔야 반영됨.
  sql = "insert into students values\
    (students_seq.nextval,:1,:2,:3,:4,\
    :5,:6,0,sysdate)"
  cursor.execute(sql,s_list)
  # sql = "insert into students values\
  #   (students_seq.nextval,:name,:kor,:eng,:math,\
  #   :kor+:eng+:math,(:kor+:eng+:math)/3,0,sysdate)"
  # cursor.execute(sql,name=name,kor=kor,eng=eng,math=math)
  conn.commit()
  conn.close()
  print("학생성적이 저장되었습니다.")
  print()

### 2.학생성적출력함수 선언
def stu_output():
  sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
  print("[ 학생성적 출력 ]")
  ###
  for s in s_title:
    print(s,end='\t')
  print()  
  print("-"*80)
  # db연결
  conn = connects()
  cursor = conn.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  print("개수 : ",len(rows))
  if len(rows)<1: 
    print("데이터가 없습니다.")
    return
  for row in rows:
    for r in row:
      print(r,end="\t")
    print()
  print()
  print("데이터 출력완료!") 