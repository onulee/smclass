# try-except-else-finally
# Exception : 모든 예외의 부모, 예외처리에서 마지막에 위치해야 함.
# as e : e변수는 예외에 대한 설명문, type(e): 예외객체
# 리스트의 범위 밖 호출 에러 : IndexError
# 입력된 값의 변환 에러 : ValueError
# raise 키워드 : 강제예외 발생

# print("프로그램을 시작합니다.")
# print("1")
# print("2")
# try:
#   print("3")
#   print("4")
#   raise NotImplementedError("프로그램을 구현해야 함.") # 프로그램을 구현되어 있지 않음.
#   # print(10/0) # 강제에러
#   print("5")
# except Exception as e:
#   print(e)
#   print("6")
#   print("7")
# finally:
#   print("8")  
#   print("9")
# print("10")
# print("프로그램을 종료합니다.")    




list1 = [52,273,32,72,100]
print(list1.index(52))


# try:
#   n_input = int(input("리스트 순번에 있는 값 출력 >> "))
#   print(f"{n_input}번째 리스트의 값 : {list1[n_input]}")
# except ValueError as e:
#   print("값을 잘못입력하셨습니다.",type(e),e)
# except IndexError as e:
#   print("번호가 범위를 벗어났습니다.",type(e),e)
# except Exception as e:
#   print("모든 예외처리의 부모")

