from django.shortcuts import render,redirect
from member.models import Member


def logout(request):
  request.session.clear()
  print("확인 : session 삭제")
  context = {"logoutmsg":"1"}
  return render(request,'index.html',context)


## 로그인페이지, 로그인확인
def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else:
    id = request.POST.get("id","")
    pw = request.POST.get("pw","")

    print("확인 : ",id,pw)

    #db에 id,pw가 있는지 확인을 해서 있으면 로그인, 없으면 다시 로그인
    qs = Member.objects.filter(id=id,pw=pw)
    if qs:
      print("id,pw가 존재합니다.")
      loginmsg = "1"
      request.session['session_id']= qs[0].id
      request.session['session_nicName']=qs[0].nicName
    else:
      print("id,pw가 존재하지 않습니다.")
      loginmsg = "0"

    context = {"loginmsg":loginmsg}
    return render(request,'login.html',context)