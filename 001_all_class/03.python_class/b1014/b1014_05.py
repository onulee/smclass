subName = ["국어","영어","수학"]
score = {"국어":100,"영어":95,"수학":80}
# print(score)
# print(score['국어'])
# print(subName[0])
# print(score[subName[0]])

for k,v in score.items():
  print(k,":",v)

for i in subName:
  print(i,":",score[i])





# def gugudan(n):
#   for i in range(2,n+1):
#     print("[ {} 단 ]".format(i))
#     for j in range(2,9+1):
#       print("{} * {} = {}".format(i,j,i*j))


# nArr = [9,5,7]
# # 2-9, 2-5, 2-7
# # gugudan(9)
# # gugudan(5)
# # gugudan(7)

# for i in nArr:
#   gugudan(i)
#   print("-"*50)


# def gugudan(n1,n2):
#   for i in range(n1,n2+1):
#     print("[ {} 단 ]".format(i))
#     for j in range(2,9+1):
#       print("{} * {} = {}".format(i,j,i*j))

# gugudan(2,5)      
# gugudan(3,9)      
# gugudan(5,8)      




# 구구단을 출력하시오.,
# 2-5
# for i in range(2,5+1):
#   print("[ {} 단 ]".format(i))
#   for j in range(2,9+1):
#     print("{} * {} = {}".format(i,j,i*j))
# # 3-9
# for i in range(3,9+1):
#   print("[ {} 단 ]".format(i))
#   for j in range(2,9+1):
#     print("{} * {} = {}".format(i,j,i*j))

# # 5-8
# # 3-9
# for i in range(5,8+1):
#   print("[ {} 단 ]".format(i))
#   for j in range(2,9+1):
#     print("{} * {} = {}".format(i,j,i*j))