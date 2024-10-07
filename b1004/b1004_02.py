
# 10번도전에서 
# 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다.
# 10번 도전에서 맞추지 못하면 , 10번도전에 실패했습니다. 랜덤숫자 : 10
# 도전에 성공했습니다. 랜덤숫자 : 10

import random

# 랜덤숫자 : 1-100
r_num = random.randint(1,100)
print("정답숫자 :",r_num)
i = 0     # 반복횟수 변수
count = 0 # 확인하는 변수
while(i<10):
  num = int(input(f"{(i+1)}번째 숫자를 입력하세요."))
  if r_num < num:
    print("입력한 숫자가 더 큽니다. 작은 수를 입력하세요.")
  elif r_num > num:
    print("입력한 숫자가 더 작습니다. 큰 수를 입력하세요.")
  else:
    print(f"정답입니다. 랜덤숫자 : {r_num}")
    count = 1
    break
  i += 1

if count == 0:
  print(f"10번도전에 실패했습니다. 랜덤숫자 : {r_num}")
