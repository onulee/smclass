from django.shortcuts import render
from member.models import Member
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입

def idChk(request):
  id = request.POST.get("id","")
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  if not qs:
    context = {"result":"success"}
  else:
    context = {"result":"fail","member":qs_list}
  return JsonResponse(context)


# 회원가입 03
def step03(request):
  return render(request,'step03.html')

## json타입 변경 - list,dic타입  qs:set -> list타입변경
## 로그인체크
## @csrf_exempt :: 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw) # 없으면 None
  if qs:
    print("성공")
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    qs_list = list(qs.values())
    context = {"result":"success","member":qs_list}
  else:
    print("실패")
    context = {"result":"fail"}  
    
  # qs = Member.objects.get(id=id,pw=pw)    # 없으면 에러  
  # json_qs = serializers.serialize('json',[qs]) #json타입변경  
    
  return JsonResponse(context)

## 로그인페이지
def logout(request):
  request.session.clear()  #모두 삭제, del request.session['session_id'] 1개 삭제 
  context = {"outmsg":"1"}
  return render(request,'index.html',context)

## 로그인페이지
def login(request):
  return render(request,'login.html')
