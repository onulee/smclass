from django.shortcuts import render,redirect
from member.models import Member

# 로그아웃
def logout(request):
  request.session.clear()
  return redirect("/")

# 로그인페이지 열기, 로그인확인
def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    
    if qs: # Member 있을 경우
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
      context = {"lmsg":"1"}
    else:  # Member 없을 경우
      context = {"lmsg":"0"}
    
    return render(request,'login.html',context)   
      