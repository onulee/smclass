import datetime
# 현재년도
print(datetime.datetime.now().year)
nowYear = datetime.datetime.now().year
# in_year = input("생일입력 : 20020312")

in_year = "20020312"
print(in_year)
print(int(in_year[:4]))
print(f"현재 나이 : {nowYear-int(in_year[:4])}")
