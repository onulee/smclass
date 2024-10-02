# 문자열

# 문자열숫자
a = "123"
print(type(a))       #str
print(type(int(a)))  #int
print(type(float(a))) #float

b = "12.3"
# print(type(int(b))) #에러 - 소수점이 있는 문자열숫자는 float변경해야 함.
print(type(float(b))) #float


# 문자열연결연산자 +
s1 = "안녕"
s2 = "안녕하세요."
print(s1+s2)
print(a+b)   # 문자열연결연산자 +
# print(a*b)   #에러 : 문자열은 -,*,/ 안됨.

# 문자열 * 2 # 문자열반복연산
print("안녕"*10)
print("-."*30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다." # 문자열자체 - 리스트 형태
print(str1[0])   # 해당번호 넣으면 해당되는 문자출력
print(str1[6])
print(str1[2:5]) # 해당범위출력 : [위치:위치한칸뒤]
print(str1[:5])  # [처음:숫자앞까지]
print(str1[2:])  # [위치:끝까지]
print(str1[1:10:2]) #[위치:숫자앞까지:step2]
print(str1[1:10:3]) #[위치:숫자앞까지:step3]
print(str1[::-1])   #[처음:끝까지:역순으로]

# [] - 배열 : 배열은 한번 범위가 정해지면 수정이 불가능 : c,자바
# [] - 리스트 : 범위상관없음.


c = 12.3
print(type(int(c))) #실수는 int타입으로 변경이 가능함.
print(int(c))


# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을때
# if input_str != "": # 빈공백이 아니냐?
#   print("입력문자 : ",input_str)  
#   print("프로그램이 종료됩니다.")
# else:
#   print("글자를 입력하셔야 합니다.")
