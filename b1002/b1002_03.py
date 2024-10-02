# if - else
# if elif else
# 100~98 A+ / # 97~94 A / # 93~90 A-
# 89~88 B+ / # 87~84 B / # 83~80 B-
# 70점대 C / # 60점대 D / # 60점이만 F
num = int(input("숫자를 입력하세요."))
score = ""

if 90<= num:
  score = "A"
  if 98<= num:
    score += "+"
  elif 90<= num <=93:
    score +="-"  
elif 80<= num:
  pass

if 98 <= num:
  print("A+")
elif 94 <= num:
  print("A") 
elif 90 <= num:
  print("A-") 
elif 98 <= num:
  print("B+") 
elif 84 <= num:
  print("B") 
elif 80 <= num:
  print("B-") 
else:
  print("F")  



# 숫자를 입력받아
# 3,4,5 - 봄, 6,7,8-여름, 9,10,11-가을, 12,1,2 - 겨울입니다.
# 그 외 숫자 - 잘못된 월이 입력되었습니다. 출력하시오.
# num = int(input("숫자를 입력하세요."))
# if 3<= num <=5: # 3<=num and num<=5
#   print("봄입니다.")
# elif 6<= num <= 8:
#   print("여름입니다.")  
# elif 9<= num <= 11:
#   print("가을입니다.")  
# elif 1<= num <= 2 or num==12:
#   print("겨울입니다.")  



# 입력한 숫자가 10(10포함)보다 작거나, 100(100포함)보다 
# 클때 정답입니다. 오답입니다. 출력하시오.
# num = int(input("숫자를 입력하세요."))
# if num<=10 or num>=100:
#   print("정답입니다.")
# else:
#   print("오답입니다.")  




# 입력한 숫자가 1(포함)보다 크고 10(10포함)보다 작을때만 
# 1 <= x <= 10
# 정답입니다. 오답입니다.
# num = int(input("숫자를 입력하세요."))
# if num <= 1 and num >= 10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")

# if 1<= num <=10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")      





# # 입력한 숫자가 짝수인지, 홀수인지 출력하시오.
# num = int(input("숫자를 입력하세요."))

# if num%2 == 0:
#   print("짝수입니다.")
# else:
#   print("홀수입니다.")
    