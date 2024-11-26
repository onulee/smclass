from django.shortcuts import render
from board.models import Board
from member.models import Member
from datetime import datetime
from django.db.models import Q
from django.db.models import F

# 글수정
def bupdate(request,bno):
  qs = Board.objects.get(bno=bno)
  context = {"board":qs}
  return render(request,'bupdate.html',context)



# 글삭제
def bdelete(request,bno):
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request,'blist.html',context)

# 글상세보기
def bview(request,bno):
  qs = Board.objects.get(bno=bno)
  
  ## 이전글, 다음글
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep) | Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()
  next_qs = ""
  
  
  ## 조회수 증가 방지, 날짜 설정 - 쿠키기간사용
  day1 = datetime.replace(datetime.now(),hour=23,minute=59,second=59)
  expires = datetime.strftime(day1,"%a, %d-%b-%Y %H:%M:S GMT")
  print("날짜 : ",expires)
  context = {"board":qs,"prev_board":prev_qs,"next_board":next_qs}
  response = render(request,'bview.html',context)
  ## 쿠키확인
  if request.COOKIES.get("cookie_boardNo") is not None:
    cookies = request.COOKIES.get("cookie_boardNo")   # 1|5|6|2
    cookies_list = cookies.split("|")
    if str(bno) not in cookies_list:
      ## 쿠키저장
      response.set_cookie("cookie_boardNo",cookies + f"|{bno}",expires=expires)
      ## 조회수 1증가
      qs.bhit += 1
      qs.save()
      
  else:
    ## 쿠키저장
    response.set_cookie("cookie_boardNo",bno,expires=expires)
    ## 조회수 1증가
    qs.bhit += 1
    qs.save()
  
  return response



# 게시판글쓰기페이지, 글쓰기 저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")
    print("파일정보 : ",bfile)
    # 글쓰기 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()
    
    context = {'wmsg':"1"}
    return render(request,'bwrite.html',context)


# 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
