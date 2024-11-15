from django.shortcuts import render,redirect
from students.models import Student

def list(request):
  # 학생전체리스트 가져오기
  qs = Student.objects.all()
  # 정보전달 변수생성
  context = {"list":qs}
  return render(request,'list.html',context)

## 1.write페이지 열기,2.write 학생정보 저장
def write(request):
  if request.method == "GET":
    print("write GET방식 호출")
    return render(request,'write.html')
  else:
    print("write POST방식 호출")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    # qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    # qs.save()
    return redirect('index')
