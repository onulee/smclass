subject = ["국어","영어"]
score = []

while True:
  print("1.과목추가")
  print("0.종료")
  choice = input("원하는 번호를 입력하세요>> ")
  if choice == "1":
    s_input = input("과목을 추가하세요.>>")
    subject.append(s_input)
  elif choice == "0":
    break

for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요.>> ")))

sum = 0
for i in range(len(subject)):
  print(f"{subject[i]} :",score[i])
  sum += score[i]
print("합계 :",sum)




# # 함수선언
# def output(subject):
#   # 출력
#   print("과목")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>> ")
#   # list - append
#   subject.append(s_input)
#   output(subject)  # 출력함수호출
  




# a = 10
# b = 20
# c = 30

# # 함수를 사용해서, a+b+c의 합 a에 저장해서 출력하시오.
# def add(a,b,c):
#   a = a+b+c
#   print(a)

# add(a,b,c)
# print(a)



# a = 10
# b = 20
# sum = 0

# # 함수선언
# def add(a,b):
#   return a+b

# sum = add(a,b) #함수호출
# print("a+b 합계 : ",sum)




# a = 10 # 전역변수

# # 함수선언
# def func(a):
#   print("함수내 a :",a)
#   a += 50
#   return a
#   # global a  # 전역변수를 가져옴.
#   # a = 50 # 지역변수 - 함수를 종료하면 모두 제거됨.


# # 함수호출
# a = func(a)
# print("함수밖 a : ",a)





# subject = ["국어","영어"]

# # 함수선언
# def output(subject):
#   # 출력
#   print("과목")
#   print("-"*20)
#   for s in subject:
#     print(s)

# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요.>> ")
#   # list - append
#   subject.append(s_input)
#   output(subject)  # 출력함수호출
  

  
