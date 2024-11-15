s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] 
# kor = int(input('국어점수를 입력하세요.')) 
# eng = int(input('영어점수를 입력하세요.')) 
# math = int(input('수학점수를 입력하세요.')) 
# print(kor,eng,math)

score = []
for sc in range(3):
  score.append(int(input(f"{s_title[sc+2]}점수를 입력하세요.")))

print(score)