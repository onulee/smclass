import func

while True:
  # 시작화면 출력
  choice = func.screen()
  
  if choice == "1":   # 1.로그인 부분
    func.memLogin()
  elif choice == "2": # 2.비밀번호찾기 부분
    func.search_pw()
  elif choice =="3":  # 3.회원가입    
    pass

