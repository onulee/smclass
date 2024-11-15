students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"김관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순동","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강홍찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구길","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수

# 학생성적출력 함수선언
def stu_output(s_title,students):
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

# 학생성적검색함수 선언
def stu_select(s_title,students):
  while True:
    flag = 0
    print("[ 학생성적검색 ]")
    name = input("찾고자 하는 학생의 이름을 입력하세요.(0.이전화면 이동)")
    if name == "0":
      break
    sArr = [] 
    for idx,s in enumerate(students):
      if s['name'].find(name) != -1:
        # print(f"{idx} 번째,{name} 학생을 찾았습니다.", s['name'])
        sArr.append(s)
        flag = 1  
    
    if flag == 0:
      print("찾는 학생이 없습니다. ") 
    else:
      print(f"{name} 이름으로 {len(sArr)}명 검색되었습니다.")
      stu_output(s_title,sArr)    

# 학생성적검색함수 호출
stu_select(s_title,students)


# ss = "파이썬 공부는 즐겁습니다. 물론 모든 공부가 다 재미있지는 않죠"
# print(ss.find("공부"))
# print(ss.find("자바")) # 없을때 -1
# print(ss.index("공부")) 
# # print(ss.index("자바")) # 없을때 에러