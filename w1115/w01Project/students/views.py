from django.shortcuts import render

# Create your views here.

def write(request):
  return render(request,'stu_write.html')
