# members리스트 딕셔너리 저장
members = []
m_title = ['id','pw','name','nicName','address','money']

# 파일불러오기
f = open('b1017/member.csv',"r",encoding="utf-8")
while True:
  line = f.readline()
  if not line: break
  # c리스트 저장
  c = line.strip().split(",")
  c[5] = int(c[5])  # money
  # members리스트에 딕셔너리 저장
  members.append(dict(zip(m_title,c)))
f.close()

# members리스트 출력
# print(members)

while True:
  print("1.회원등록")
  print("2.회원검색")
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    id = input("ID를 입력하세요.>> ")
    flag = 0
    for m in members:
      if m['id'] == id:
        print(f"{id} 는 동일한 아이디가 있습니다. 다시 입력하세요.")
        flag = 1
        break
    if flag == 1:
      continue 
    else:
      print(f"{id} 는(은) 사용가능합니다. ")
      print() 
    pw = input("PW를 입력하세요.>> ")
    name = input("이름을 입력하세요.>> ")
    nicName = input("닉네임을 입력하세요.>> ")
    money = int(input("충전금액을 입력하세요.>> "))
    m_list = [id,pw,name,nicName,money]
    members.append(dict(zip(m_title,m_list)))
    print(f"{id} 님 회원가입이 완료되었습니다!")
    print(m_list)
    print("-"*50)
    print(members)

  elif choice == "2":
    # 회원 검색
    search = input("검색할 회원이름을 입력하세요.>> ")
    flag = 0
    mm = []
    for m in members:
      if m['id'].find(search) != -1:
        mm.append(m)
        flag = 1

    if flag == 0:
      print("검색 회원을 찾지 못했습니다. 다시 입력하세요!")    
    else:
      print("총 검색된 인원 :",len(mm))
      print(mm)

