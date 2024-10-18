# 딕셔너리로 학생을 입력하시오.
students = []
subject = ["번호","이름","국어","영어","수학","합계","평균","등수"]
sub = ["no","name","kor","eng","math","total","avg","rank"]

f = open("b1017/students.txt","r",encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  s = line.strip().split(",")
  for idx,i in enumerate(s):
    if idx == 1 : continue
    elif idx == 6: s[6] = float(i)
    else: s[idx] = int(i)
  students.append(dict(zip(sub,s)))
f.close()
print(students)
print("프로그램을 종료합니다.")
