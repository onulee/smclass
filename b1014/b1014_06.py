import random
fruit = {"바나나":"banana","오렌지":"orange","체리":"cherry",
         "파인애플":"pineapple","코코넛":"coconut"}
# fName = ["바나나","오렌지","체리","파인애플","코코넛"]
fName = list(fruit.keys())
print(fName)
# random.shuffle(tName)  # 원본이 변경이 됨.

# fName 랜덤순서로 영문퀴즈 시작
# re_fName = random.sample(fName,5)
# for i in re_fName:
#   search = input(f"{i}의 영문을 입력하세요.")
#   if fruit[i] == search:
#     print("정답입니다.",fruit[i],search)
#   else:
#     print("오답입니다.",fruit[i],search)



# fName 순서대로 영문퀴즈 시작
# print("[영단어 맞추기 ]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요.")
#   if fruit[key] == search:
#     print("정답입니다.",fruit[key],search)
#   else:
#     print("오답입니다.",fruit[key],search)


# search = input("바나나의 영문을 입력하세요.")
# if fruit['바나나'] == search:
#   print("정답입니다.",fruit['바나나'],search)
# else:
#   print("오답입니다.",fruit['바나나'],search)





# 바나나를 입력하면 영어로 banana
# print(fruit["바나나"])
# print(fruit["오렌지"])

# while True:
#   search = input("과일이름을 입력하세요.>> ")
#   if search in fruit:
#     print("영문으로 : ",fruit[search])
#   else:
#     print("찾는 단어가 없습니다.")  