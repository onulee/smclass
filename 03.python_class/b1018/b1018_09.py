# Student클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언후 저장
# 번호-자동부여, 이름,국어,영어,수학,합계,평균,등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생성적 프로그램 ]
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적수정

class Student:
  def __init__(self,no,name):
    self.no = no 
    self.name = name

students = []
s1 = Student(1,"홍길동")
print(s1.no)
s2 = Student(2,"유관순")
students.append(s1)
students.append(s2)

for s in students:
  print(s.no,s.name)
