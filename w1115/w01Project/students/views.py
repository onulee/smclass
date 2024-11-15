from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def write(request):
  print("학생등록페이지 호출")
  return render(request,'stu_write.html')

def save(request):
  print("학생정보저장")
  return HttpResponseRedirect(reverse('index'))
