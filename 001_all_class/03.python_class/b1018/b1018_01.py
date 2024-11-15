# 클래스 - 변수,함수의 집합체
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
s_t = ['no','name','kor','eng','math','total','avg','rank']

# 학생1명의 정보 - Class로 변경
# 학생전체리스트 - Class로 변경
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

print("[ 학생성적 출력 ]")
for st in s_title:
  print(st,end='\t')
print()  
print("-"*80)  
for s in students:
  for i in range(len(s_t)):
    print(f"{s[s_t[i]]}",end='\t')
  print() 

# 입력함수 선언
def stu_chg(no,name,kor,eng,math):
  return {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,"total":kor+eng+math,"avg":(kor+eng+math)/3,"rank":rank}


# 학생성적 직접 입력
print("[ 학생성적 입력 ]")
stuNo = len(students)
no = stuNo + 1  # 리스트 - 학생수
name = input(f"{no}번째 학생 이름을 입력하세요.(0.이전화면) >>")
kor = int(input("국어점수를 입력하세요."))
eng = int(input("영어점수를 입력하세요."))
math = int(input("수학점수를 입력하세요."))
students.append(stu_chg(no,name,kor,eng,math))

