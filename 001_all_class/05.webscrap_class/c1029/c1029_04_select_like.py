# employees 테이블에서 이름이 a가 포함되어 있는 이름, 모든 컬럼 출력
import oracledb

# db연결 함수선언
def connections():
  try:
    conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
    print("db연결 : ",conn.version)
  except Exception as e: print("예외발생 : ",e)
  return conn
      
# 함수호출
conn = connections()
cursor = conn.cursor()

# 범위를 입력받아서 그 사이의 사원을 출력하시오.
num1 = input("첫번째 숫자를 입력하세요.")
num2 = input("두번째 숫자를 입력하세요.")
# 월급 4000~8000사이의 사원을 모두 출력하시오.
sql = "select employee_id,emp_name,salary from employees where salary >= :num1 and salary <= :num2 order by salary"
cursor.execute(sql,num1=num1,num2=num2)

# 입력한 값을 가지고 이름이 포함되어 있는 데이터를 출력하시오.
# search = input("이름을 입력하세요.>> ")
# search = '%'+search+'%'
# sql = "select * from employees where emp_name like :search "
# cursor.execute(sql,search=search)

# search = input("번호검색 >> ")
# sql = "select * from employees where emp_name like '%:search%'"
# 키워드
# sql = "select * from employees where employee_id>=:search"
# cursor.execute(sql,search=search)
# 번호순서
# sql = "select * from employees where employee_id>=:1"
# cursor.execute(sql,[search])

title = ['employee_id','emp_name','salary']
a_list = [] # dict타입으로 변경해서 저장하시오.
rows = cursor.fetchall()
print("개수 : ",len(rows))
for row in rows:
  a_list.append(dict(zip(title,row)))
  print(row)

print(a_list)  
  
cursor.close() 



# employees테이블. emp_name a가 포함되어 있는 row모두 출력하시오.
# search = input("검색할 이름을 입력하세요.")
# search = '%'+search+'%'
# # 리스트 형태로 변경
# sql = "select * from employees where emp_name like :search"
# cursor.execute(sql,search=search)

# # %포함
# search = input("검색할 이름을 입력하세요.")
# # 리스트 형태로 변경
# sql = "select * from employees where emp_name like :1"
# cursor.execute(sql,[('%'+search+'%')])


 
