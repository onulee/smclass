import random
#### for
r_num = random.randint(1,100)
count = 0
for i in range(10):
  input_num = int(input("숫자를 입력하세요."))  #str -> int타입으로 변경
  # 비교구문
  if r_num < input_num:
    print("입력한 숫자가 큽니다.")
  elif r_num > input_num:
    print("입력한 숫자가 작습니다.")
  else:
    print("정답입니다. 정답번호 : ",r_num)
    count = 1
    break

  # 10번 도전에서 실패 할 경우
if count == 0:
  print("10번 도전에 실패하셨습니다. 정답번호 : ",r_num)


#### while
# i = 0 # 초기값
# # 랜덤숫자는 while 밖에 있어야 함.
# # while 안에 있으면 돌때마다 랜덤숫자 같이 변경
# r_num = random.randint(1,100) 
# count = 0
# while i<10: #조건식
#   input_num = int(input("숫자를 입력하세요."))  #str -> int타입으로 변경
#   # 비교구문
#   if r_num < input_num:
#     print("입력한 숫자가 큽니다.")
#   elif r_num > input_num:
#     print("입력한 숫자가 작습니다.")
#   else:
#     print("정답입니다. 정답번호 : ",r_num)
#     count = 1
#     break
#   i += 1 #증감식

#   # 10번 도전에서 실패 할 경우
# if count == 0:
#   print("10번 도전에 실패하셨습니다. 정답번호 : ",r_num)
