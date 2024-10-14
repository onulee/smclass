def stu_input(stuNo,students):
  while True:
    no = stuNo + 1
    print("no :",no)
    name = input(f"{no}번째 학생이름을 입력하세요.(0.이전페이지 이동)")
    students.append({"no":no,"name":name})
    print(students)
    stuNo += 1
    return stuNo