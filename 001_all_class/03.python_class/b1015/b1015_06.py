students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수

print("[ 학생성적 삭제 ]")
name = input("찾고자 하는 학생의 이름을 입력하세요.")
flag = 0
for idx,s in enumerate(students):
  if s['name'] == name:
    flag = 1
    print(f"{name} 학생성적을 삭제하시겠습니까?( 삭제시 복구불가 )")
    print("1.삭제 2.취소")
    choice = input("원하는 번호를 입력하세요.>> ")  
    if choice == "1":
      del students[idx]
      print(f"{name} 학생성적이 삭제되었습니다.")
    else:
      print("학생성적 삭제가 취소되었습니다.")
      break 
# 모든 학생 비교가 끝난 후, flag 확인  
if flag == 0:
  print(f"{name} 학생이 없습니다. 다시 입력하세요.")    

# stu_output(s_title,students)