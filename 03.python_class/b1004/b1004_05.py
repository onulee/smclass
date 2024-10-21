# for문을 출력
for k in range(1,10):
  print(f"[ {k} 단 ]",end="\t")
print()  
for i in range(2,10):
  for j in range(1,10):
    print(f"{j} x {i} = {j*i}",end="\t")
  print()  

# 000
# 001
# ...
# 997
# 998
# 999

# for i in range(1000):
#   print(f"{i:03d}")


# # for 3개 사용
# for i in range(10):
#   for j in range(10):
#     for k in range(10):
#       print(f"{i}{j}{k}")




# # 구구단 입력한 단까지 출력하시오.  
# # 3 -> 1,2,3단 출력 5-> 1,2,3,4,5단까지 출력
# a_input = int(input("숫자를 입력하세요"))
# for i in range(a_input,a_input+1):
#   for j in range(1,10):
#     print(f"{i} X {j} = {i*j}")