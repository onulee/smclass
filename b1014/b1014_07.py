stu_title = ['국어','영어','수학']
students = {"국어":100,"영어":100,"수학":99,"합계":299}

def s_modify(choice):
  print("현재 {}점수 : {}".format(stu_title[choice-1], students[stu_title[choice-1]]))
  students[stu_title[choice-1]] = int(input(f"변경 {stu_title[choice-1]} 점수를 입력세요."))

print("[점수수정]")
print("1.국어")
print("2.영어")
print("3.수학")
choice = int(input("수정하려는 과목을 선택하세요.>> "))
if choice == 1:
  s_modify(choice)
elif choice == 2:
  s_modify(choice)
elif choice == 3:
  s_modify(choice)

students['합계'] = students["국어"]+students["영어"]+students["수학"]
print("변경 : ",students)  





