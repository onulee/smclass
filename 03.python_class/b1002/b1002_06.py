students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99]
]
ss = [4,'강감찬',100,90,99]

# students 에 ss를 추가하시오.
students.append(ss)
print(students)


# 값이 2개 이상 저장하려면, 주소값
# 이순신인 데이터를 삭제하시오.
# del 삭제
for idx,s in enumerate(students):  
  if s[1] == '이순신':
    del students[idx]       # del로 삭제


# 삭제 - remove    
# for s in students:  # [1,'홍길동',100,90,99],[2,'유관순',100,100,99],[3,'이순신',100,100,99]
#   if s[1] == '이순신':
#     students.remove(s) # remove
    
print(students)


# print(students) # 한번에 모두 출력

# for s in students: # 1개씩 가져와서 출력
#   print(s)

# # 이름이 유관순인것을 출력하시오.
# for s in students: # 1개씩 가져와서 출력
#   if s[1] == '유관순':
#     print(s)

