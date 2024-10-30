import random
import oracledb
import smtplib
from email.mime.text import MIMEText

def connects():
  user="ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 : ",e)  
  return conn


while True:
  print("[ 커뮤니티 ]")
  print("1. 로그인")
  print("2. 비밀번호 찾기")
  print("3. 회원가입")
  print("0. 프로그램 종료")
  print("-"*30)
  choice = input("원하는 번호를 입력하세요.>> ")
  
  if choice == "1":
    print("[ 로그인 ]")
    user_id = input("아이디를 입력하세요.>> ")
    user_pw = input("패스워드를 입력하세요.>> ")
    # db접속
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id and pw=:pw"
    cursor.execute(sql,id=user_id,pw=user_pw)
    row = cursor.fetchone() # None
    print(row)
    if row != None:
      print(f"로그인 성공! {row[2]} 님 환영합니다.")
    else:
      print("아이디 또는 패스워드가 일치하지 않습니다. 정확히 입력하세요!! ")  
    cursor.close()
    
    # 오라클db에 접속해서 member테이블에서 검색 가져옴.
    # if user_id == 'aaa' and user_pw == "1111":
    #   print("로그인 성공")
    # else:
    #   print("로그인 실패")
    #   continue
      
    print("[ 학생성적 프로그램에 접속합니다. ]")  
    ### 프로그램 구현 ###  
    
  elif choice == "2":
    print("[ 비밀번호 찾기 ]")
    search = input("해당 아이디를 입력하세요.>> ")
    # 아이디 있는지 확인
    conn = connects()
    cursor = conn.cursor()
    sql = "select * from member where id=:id"
    cursor.execute(sql,id=search)
    row = cursor.fetchone()
    print(row)
    if row != None:
      print("아이디가 존재합니다. 임시패스워드를 발급합니다.")
      # 1. 임시비밀번호를 생성해서
      # 2. 이메일로 보냅니다.
      # 3. 아이디에 비밀번호를 임시비밀번호를 수정합니다.
      # 4. 임시번호로 로그인을 했을 경우 로그인 성공이 나타나도록 하시오.
      
      
      #### 메일발송 ####
      email = row[3]
      
      # 1. 임시비밀번호 생성
      a = random.randrange(0,100000000) # 0-9999
      ran_num = f"{a:08}"
      # 랜덤4자리 숫자
      print(ran_num)
      
      # 2. 임시비밀번호를 수정
      # user_id = row[0]
      sql = "update member set pw=:pw where id=:id"
      cursor.execute(sql,id=search,pw=ran_num)
      
      # email 발송관련
      smtpName = "smtp.naver.com"
      smtpPort = 587

      # 자신의 네이버메일주소,pw, 받는사람이메일주소
      sendEmail = "onulee@naver.com"
      pw = "1LDN53XPJ58R9"
      recvEmail = email

      title = "제목 : [ 메일발송 ] 임시번호 발송"
      content = f"{ran_num}"

      # 설정
      msg = MIMEText(content)
      msg['Subject'] = title
      msg["From"] = sendEmail
      msg['To'] = recvEmail
      print("msg 데이터 : ",msg.as_string())

      # 서버이름,서버포트
      s = smtplib.SMTP(smtpName,smtpPort)
      s.starttls()
      # 2단계 보안설정이 되어 있는 경우는 에러 발생
      # 인증키 발급을 받아야 함.
      s.login(sendEmail,pw)
      s.sendmail(sendEmail,recvEmail,msg.as_string())
      s.quit()

      # 메일발송 완료
      print("메일을 발송했습니다.")
      
      
    else:
      print("아이디가 존재하지 않습니다.")  
    
    cursor.close()
    
  elif choice == "3":
    pass
  elif choice == "0":
    print("프로그램 종료합니다.")
    break