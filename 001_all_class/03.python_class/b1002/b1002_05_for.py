students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]

print(len(students))

# 반복문
for i in range(10):  # 시작:0해서 10번반복
  print(i)

for i in range(2,5): # 시작:2부터 5이전까지 반복
  print(i) 

for i in range(1,10,2): # 시작:1부터 10이전까지 step2해서 출력
  print(i)   

aArr = [1,2,5,7,8]
for i in aArr:  # list의 값을 1개씩 가져와서 출력
  print(i)

for i,data in enumerate(aArr):  # list의 값과 index번호를 함께 출력
  print(i,":",data)


aStr = "안녕하세요"
for i in aStr: # 문자열의 값을 1개씩 가져와서 출력
  print(i)

# enumerate index번호를 추가해서 가져올수 있음.
for idx,data in enumerate(aStr):
  print(idx,":",data)  

 

  

# #    번호,이름,국어,영어,수학
# s = [4,'강감찬',100,90,99]
# print(s[2]) 
# # s 리스트에 합계,평균을 추가하시오.
# s.append(s[2]+s[3]+s[4])
# s.append((s[2]+s[3]+s[4])/3)
# print(s)




# list 추가 - append-뒤에추가,insert-원하는 위치추가
# 삭제 del-위치삭제,remove-값으로 검색해서 삭제
# a_list = [1,2,3]
# # 10추가 
# a_list.append(10) # 마지막에 10추가
# print(a_list)

# a_list.insert(2,100) #index 2번에 100추가
# print(a_list)

# del a_list[1]     # index 1번 삭제
# print(a_list)

# a_list.remove(100) # 100이라는 값으로 삭제
# print(a_list)

# 문자열 슬라이싱
# str = "좋은 하루되세요. 많은 행복받으세요. 많은 감사! 많은 돈"
# print(len(str))

# # 뒤쪽에서 5자리 전까지 출력
# print(str[-5:])
# print(str[-1])
# print(str[::-1])
