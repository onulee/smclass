# 정렬
n_lists = [
  ["john",100,4.5,1000],
  ["park",80,4.2,800],
  ["lee",90,4.4,2000],
  ["trumf",200,4.7,10],
  ["bill",30,4.3,30]
]

print("기본 :",n_lists)
# n_lists 에서 1개(n_list) x대입
n_lists.sort(key=lambda x:x[1],reverse=True)
print("이름정렬 :", n_lists)





# a = ""
# print(int(a))
# print("완료")






# a = "안녕하세요"
# print(a[1:])
# print(a[1:-1])
# print(a[:3])
# print(a[::-1])

# lists = [1,2,3,4,5,6,7,8,9]
# print(lists[1:-1])
# print(lists[:-1])
# print(lists[3:])
# print(lists[3:5])
# print(lists[::-1])


# b = 12345
# print(b[1,-1])
