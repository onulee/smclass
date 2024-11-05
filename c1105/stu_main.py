import oracledb
import stu_func

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

while True:
  choice = stu_func.main_print()   ## 메인화면출력부분
  if choice == "1":
    stu_func.stu_insert()          ## 학생성적입력부분
  elif choice == "2":
    stu_func.stu_output()          ## 학생성적출력부분  
  elif choice == "3":
    print("[ 학생성적 검색 ]") 
    print("1. 이름으로 검색")
    print("2. 합계순 검색")
    choice = input("원하는 번호를 입력하세요.>> ")
    if choice == "1":
      print("[ 이름으로 검색 ]") 
      search = input("찾고자 하는 이름을 입력하세요.>> ")
      search = '%'+search+'%'
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
             rank,to_char(sdate,'yyyy-mm-dd') \
             from students where name like :search"
      
      ##### 출력부분 #####
      # db연결
      conn = stu_func.connects()
      cursor = conn.cursor()
      cursor.execute(sql,search=search)
      rows = cursor.fetchall()
      print(f"[ 개수 : {len(rows)} ]")
      for s in s_title:
        print(s,end='\t')
      print()  
      print("-"*80)
      if len(rows)<1: 
        print("데이터가 없습니다.")
        break
      for row in rows:
        for r in row:
          print(r,end="\t")
        print()
      print()
      print("데이터 출력완료!")  
  elif choice == "4":
    print("[ 학생성적 정렬 ]")
    print("1.이름순차정렬")      
    print("2.이름역순정렬")
    print("2.이름역순정렬")
    choice  = input("원하는 번호를 입력하세요.>> ") 
    if choice == "1":
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
             rank,to_char(sdate,'yyyy-mm-dd') \
             from students order by name"
    elif choice == "2":
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
             rank,to_char(sdate,'yyyy-mm-dd') \
             from students order by name desc"
    elif choice == "3": #합계순차정렬
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
             rank,to_char(sdate,'yyyy-mm-dd') \
             from students order by total"
    elif choice == "4": #합계역순정렬
      sql = "select no,name,kor,eng,math,total,round(avg,2),\
             rank,to_char(sdate,'yyyy-mm-dd') \
             from students order by total desc"
           
    ##### 출력부분 #####
    # db연결
    conn = stu_func.connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for s in s_title:
      print(s,end='\t')
    print()  
    print("-"*80)
    if len(rows)<1: 
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!") 
    
  elif choice =="5":
    print("[ 학생등수처리 ]")
    sql = "update students a set rank = (\
          select ranks from \
      ( select no,rank() over(order by avg desc) ranks from students\
      ) b where a.no = b.no )"
      
    ##### 출력부분 #####
    
    # db연결
    conn = stu_func.connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("등수처리가 완료되었습니다.")
    print()
    #----------------------------------
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for s in s_title:
      print(s,end='\t')
    print()  
    print("-"*80)
    if len(rows)<1: 
      print("데이터가 없습니다.")
      break
    for row in rows:
      for r in row:
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")  
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



