ss = "파이썬 수업중 타입 문자열 타입,정수형 타입,실수형 타입,논리형 타입이 있습니다"

sss = ss.replace("타입","atype")
print(sss)

a_str = "파이썬"
a = "-".join(a_str)
print(a)


# idx = 0
# search = input("검색할 단어를 입력하세요. >> ")
# a_list = []
# for i in range(ss.count(search)):
#   num = ss.find(search,idx) #0번부터시작 - 8, 15, 22, 29, 36
#   a_list.append(num)
#   idx = num+1

# print(f"검색개수 : {len(a_list)}, 위치값 : {a_list}")


# i_str = input("글자를 입력하세요.")


# # 검색 글자 개수
# idx = ss.count(i_str)
# print("개수 :",idx)

# # 타입의 위치값을 모두 출력하시오.
# for s in range(ss.count(i_str)):



# 위치값 - find 없을때 -1
# idx = ss.find(i_str)
# print("위치값 :",idx)
# index - 위치값, 없을때 에러
# idx = ss.index(i_str)
# print("위치값 :",idx)



# if i_str in ss:
#   print("있습니다.")
# else:
#   print("없습니다.")  




# # 1-20 중에 3의 배수만 리스트에 추가하시오.
# a_list = []
# for i in range(1,21):
#   if i%3 == 0:
#     a_list.append(i)

# print(a_list)

# # 리스트 내포
# # [ 값 for문 조건식 ]
# b_list = [ i for i in range(1,21) if i%3 == 0]
# print(b_list)




#  aArr = [1,2,3,4,5]
# a_list = []
# # 1줄 for문으로 a_list = [1,4,9,15,25]

# a_list = [i*i for i in aArr]
# print(a_list)



# stu_print() # 모듈
# if choice == "1":
#   stu_input()
# elif choice =="2":
#   stu_output()
# elif choice == "3":
#   stu_update()    