# 0부터 1씩 증가하면서, 10번 실행
for i in range(10):
  print(i)
print("-"*50)
# 5부터 9(10이전)까지 실행
for j in range(5,10):
  print(j)  

# (시작값,끝값+1,증가값)
for i in range(1,10,2):   
  for j in range(1,10):
    print(f"{i} x {j} = {i*j}")


print("-"*50)
a_list = [1,2,3,4,5]
for k in a_list:
  print(k)

# 파이썬 - 문자열-str,정수형-int,실수형-float,논리형-bool
# 리스트타입 - []
b_list = [3,5,9,10,20,3,3,10,5,20]
for m in b_list:
  print(m)

# 딕셔너리타입 - {} : json타입과 모양이 같음. 키,값(key,value)
dic = {
  "번호":1,"이름":"홍길동","국어":100,"영어":100,
  "수학":99
}
print(dic["번호"])
print(dic["이름"])

for n in dic: # dic에서 key값을 n에 넣어줌.
  # print(n)      # key값이 출력이 됨.
  print(dic[n]) # key값의 value값이 출력이 됨


# 리스트 길이 : len()
print(len(b_list))

# 리스트 안에 해당되는 숫자가 몇개 인지 확인 - count
print(b_list.count(5))

# 리스트 추가 - append,insert,extend([2,3])-리스트를 추가
# 리스트 삭제 - del,remove,clear-모두삭제