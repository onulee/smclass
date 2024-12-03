from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member

## 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")

## 로그인확인
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  # db확인
  qs = Member.objects.filter(id=id,pw=pw)
  print("확인 : ",id,pw)
  if qs:
    # 섹션추가
    request.session['session_id'] = qs[0].id
    request.session['session_nicName'] = qs[0].nicName
    list_qs = list(qs.values())
    context = {"result":"success","member":list_qs}  #dic,list타입
  else:
    context = {"result":"fail"}
  return JsonResponse(context)

## 로그인페이지
def login(request):
  return render(request,'login.html')
