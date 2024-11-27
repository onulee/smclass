from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse 
from member.models import Member

def join01(request):
  return render(request,'join01.html')

def join02(request):
  return render(request,'join02.html')

# ajax통신
def idChk(request):
  id = request.POST.get("id","")
  print("id : ",id)
  context = {"id":id,"result":"success"} 
  return JsonResponse(context)



# ajax통신
# @csrf_exempt #csrf_token 예외처리
def loginChk(request):
  # {"name":"kim","age":20}
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print("html에서 넘어온 데이터 : ",id, pw)
  # filter검색 객체 보내는 방법 - list타입으로 보내야 함. (타입에러 발생)
  # qs = list(Member.objects.get(id=id,pw=pw).values())
  # if qs:
  #   context = {"member":qs,"result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)
  
  # filter검색 객체 보내는 방법 - list타입으로 보내야 함. (타입에러 발생)
  qs = list(Member.objects.filter(id=id,pw=pw).values())
  if qs:
    context = {"member":qs,"result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)
  
  # # 변수보내는 방법 
  # qs = Member.objects.filter(id=id,pw=pw)
  # if qs:
  #   context = {"id":qs[0].id,"nicName":qs[0].nicName,"result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

# 로그인
def login(request):
  return render(request,'login.html')
