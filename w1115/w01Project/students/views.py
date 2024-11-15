from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from students.models import Student

### 학생전체리스트 호출
def list(request):
  # 학생전체리스트 가져오기
  qs = Student.objects.all()
  # 정보전달 변수생성
  context = {"list":qs}
  return render(request,'stu_list.html',context)

### 학생입력페이지 호출
def write(request):
  print("학생등록페이지 호출")
  return render(request,'stu_write.html')

### 학생입력저장
def save(request):
  print("학생정보저장 호출")
    
  # if request.method == 'POST': # POST방식으로 왔는지 체크
  if request.POST:  # request.POST 데이터가 있는지 체크
    print("POST방식 호출")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    # qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    # qs.save()
  return HttpResponseRedirect(reverse('index'))
  # return redirect('index')   
  # redirect('/')
  # return redirect(reverse('index')) #reverse : app_name  

