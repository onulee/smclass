
choice = 0 # 전역변수

while True:
  print("[ 학생성적 프로그램 ]")
  print("-"*60)
  print("1.학생성적입력")
  print("2.학생성적출력")
  print("3.학생성적수정")
  print("4.학생성적검색")
  print("5.학생성적삭제")
  print("6.등수처리")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.>> ")
  if choice == "1":
    print("[ 학생성적 입력 ]")
    print()
  elif choice == "2":
    print("[ 학생성적 출력 ]")  
    print()
  elif choice == "0":
    print("[ 프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break

