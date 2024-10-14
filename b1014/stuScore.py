# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수

# 메뉴출력함수 시작
def title_program():
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("7. 학생성적정렬")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")
  return choice
# --------------------

# 학생성적입력함수 시작 - 일반변수 변경
def stu_input(stuNo):
  while True:
      print("[ 학생성적 입력 ]")
      # 학생성적 직접 입력
      no = stuNo + 1  # 리스트 - 학생수
      name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
      if name == "0":
        print("성적입력을 취소합니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      ss = { "no":no,"name":name,"kor":kor,"eng":eng,
             "math":math,"total":total,"avg":avg,"rank":rank }
      students.append(ss)
      stuNo += 1  # 학생수 1증가
      print(f"{name} 학생성적이 저장되었습니다.!")
      print()

  return stuNo  

# --------------------



# 학생성적프로그램
while True:
  choice = title_program()        # 메뉴출력함수 호출
  if choice == "1":
    stuNo = stu_input(stuNo)                   # 학생성적입력함수 호출
  elif choice == "2":
    print("[ 학생성적 출력 ]")
    print()

    # 상단출력
    for st in s_title:
      print(st,end="\t")
    print(); print("-"*60) 
    
    # 학생성적출력
    for s in students:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
  
  #-----------------------
  # 3,4,5,6
  elif choice == "3":
    print("[ 학생성적수정 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.")
    chk = 0
    for s in students:
      if s[1] == name:
        # 학생성적 수정
        print(f"{name} 학생을 찾았습니다.")
        print()
        print("[ 수정 과목 선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        choice = input("원하는 번호를 입력하세요.>> ")
        if choice == "1":
          print("이전 국어점수 : {}".format(s[2]))
          s[2] = int(input("변경 국어점수 : "))
        elif choice == "2":
          print("이전 영어점수 : {}".format(s[3]))
          s[3] = int(input("변경 영어점수 : "))
        elif choice == "3":
          print("이전 수학점수 : {}".format(s[4]))
          s[4] = int(input("변경 수학점수 : "))

        s[5] = s[2]+s[3]+s[4]  # 합계
        s[6] = s[5]/3          # 평균

        print(f"{name} 학생 성적이 수정되었습니다.")
        print()
        
        # 학생출력
        # 상단타이틀 출력
        for title in s_title:
          print(f"{title}\t",end="")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
        print()
        chk = 1 

    # 모든 학생 비교가 끝난 후, chk 확인  
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")   
    print()
  elif choice == "4":
    print("[ 학생성적검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.")
    chk = 0
    for s in students:
      if s[1] == name:
        # 학생출력
        # 상단타이틀 출력
        for title in s_title:
          print(f"{title}\t",end="")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
        print()
        chk = 1 

    # 모든 학생 비교가 끝난 후, chk 확인  
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")   

  elif choice == "5":
    print("[ 학생성적 삭제 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.")
    chk = 0
    for idx,s in enumerate(students):
      if s[1] == name:
        chk = 1 
        choice = input(f"{name} 학생성적을 삭제하시겠습니까?(삭제시 복구불가)\n1.삭제 2.취소")  
        if choice == "1":
          del students[idx]
          print(f"{name} 학생성적이 삭제되었습니다.")
        else:
          print("학생성적 삭제가 취소되었습니다.")
          break  

    # 모든 학생 비교가 끝난 후, chk 확인  
    if chk == 0:
      print(f"{name} 학생이 없습니다. 다시 입력하세요.")   
  
  elif choice == "6":
    print("[ 등수처리 ]")
    for s in students:
      count = 1
      for st in students:
        if s[5] < st[5]:
          count += 1
      s[7] = count # 등수입력
    print("등수처리가 완료되었습니다.")
    print()  

  


  #-----------------------
  elif choice == "7":
    while True:
      print("[ 학생성적 정렬 ]")
      print("1. 이름 순차정렬")
      print("2. 이름 역순정렬")
      print("3. 합계 순차정렬")
      print("4. 합계 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지 이동")
      print("-"*40)
      choice = input("원하는 번호를 입력하세요.>> ")

      if choice == "1":
        students.sort(key=lambda x:x['name'])
      elif choice == "2":
        students.sort(key=lambda x:x['name'],reverse=True)
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break

      print("정렬이 완료되었습니다.")

  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break    












# 학생성적 입력부분을 구현하시오.
# dict타입으로 입력을 할것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.
