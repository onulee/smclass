import oracledb

# db연결 함수선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521:xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e : print("예외처리 : ",e)
  return conn


while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적검색")
  print("0. 프로그램종료")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    conn = connects()
    cursor = conn.cursor()
    print("[ 학생성적 입력 ]")
    sql = "select students_seq.currval from dual"
    cursor.execute(sql)
    row = cursor.fetchone()
    cursor.close()
    no = row[0]
    name = input(f"{no}번 학생이름을 입력하세요.>> ")
    kor = int(input("국어점수를 입력하세요.>> "))
    eng = int(input("영어점수를 입력하세요.>> "))
    math = int(input("수학점수를 입력하세요.>> "))
    
  elif choice == "2":
    pass
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램을 종료합니다.")
    break







# 학생성적프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# students테이블 사용해서
# 시퀀스 students_seq 생성
# 번호,김유신,99,98,96 합계,평균,등수,입력일
### 시작 ###



