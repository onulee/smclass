#  함수선언
def calc(num,num2,op):
  result = 0
  if op == "+":
    result = num + num2
  elif op == "-":
    result = num - num2
  elif op == "*":
    result = num * num2
  else:
    result = num / num2

  return result        

num = int(input("숫자를 입력하세요."))
num2 = int(input("숫자를 입력하세요."))
op = input("+,-,*,/ 하나를 선택하세요.")

print("결과값 :",calc(num,num2,op))