from django.shortcuts import render
from board.models import Board
from member.models import Member
from comment.models import Comment
from django.http import HttpResponse 
from django.http import JsonResponse,HttpResponse
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.db.models import Count
from django.db.models import QuerySet

## 카카오 지도 api 불러오기
def map(request):
  return render(request,'map.html')

## 게시글 좋아요 기능
def likes(request):
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  
  if board.like_members.filter(pk=id).exists():
    board.like_members.remove(member)
    result = "remove"
  else:
    board.like_members.add(member)  
    result = "add"
  print("개수 : ",board.like_members.count())
    
  # 데이터저장
  context = {"result":result,"count":board.like_members.count()}
  return JsonResponse(context)


## form
def form(request):
  if request.method == "GET":
    return render(request,'form.html')
  else:
    file1 = request.FILES.get('bfile')
    print("file1 : ",file1)
    file_list = request.FILES.getlist('bfile')
    print("파일 : ",file_list)
    return HttpResponse(file_list) 

## 게시글 답글달기
def breply(request,bno):
  if request.method == "GET":
    nowpage = request.GET.get("page",1)
    qs = Board.objects.get(bno=bno)
    context = {"board":qs,"nowpage":nowpage}
    return render(request,'breply.html',context)
  else:
    nowpage = request.POST.get("page",1)
    id = request.session["session_id"]
    member = Member.objects.get(id=id)
    bgroup = request.POST.get("bgroup")
    bstep = int(request.POST.get("bstep")) # 문자 -> int타입변경
    bindent = int(request.POST.get("bindent")) # 문자 -> int타입변경
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    bfile = request.FILES.get('bfile')

    # 검색 2가지
    # Board.objects.get(bno=bno)
    # qs.save()
    # Board.objects.filter(bno=bno) : 여러개       
    # update()

    # 부모보다 큰 bstep 1증가 - 
    qs = Board.objects.filter(bgroup = bgroup, bstep__gt = bstep)  # bstep > bstep
    qs.update(bstep = F("bstep")+1)

    Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile )
    context = {"rmsg":"1","nowpage":nowpage}
    return render(request,'breply.html',context)


## 게시글 수정
def bupdate(request,bno):
    if request.method == "GET":
        qs = Board.objects.get(bno=bno)
        nowpage = request.GET.get("page",1)
        context = {"board":qs,"nowpage":nowpage} 
        return render(request,'bupdate.html',context)
    else:
        nowpage = request.POST.get("page",1)
        bno = request.POST.get("bno")
        btitle = request.POST.get("btitle")
        bcontent = request.POST.get("bcontent")
        bfile = request.FILES.get("bfile","")
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        if bfile:
            qs.bfile = bfile
        qs.save()
        context = {"umsg":"1","nowpage":nowpage}
        return render(request,'bupdate.html',context)    


## 게시글삭제
def bdelete(request,bno):
    qs = Board.objects.get(bno=bno)
    qs.delete()
    context = {"dmsg":bno}
    return render(request,'blist.html',context)


## 게시글 상세보기
def bview(request,bno):
  nowpage = request.GET.get("page",1)
  qs = Board.objects.get(bno=bno) # 현재글
  qs.bhit = qs.bhit + 1
  qs.save()
  
  ## 이전글,다음글 포함
  next_qs = Board.objects.filter\
      (Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep)\
      |Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by("-bgroup","bstep").last()
  prev_qs = Board.objects.filter\
      (Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)\
      |Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()
  print("이전글 :",prev_qs.bno)

  # 하단댓글가져오기 포함
  c_qs = Comment.objects.filter(board=qs).order_by("-cno")
  print("확인 : ",c_qs,c_qs.count)
  context = {"board":qs,"clist":c_qs,"nowpage":nowpage,"next_board":next_qs,"prev_board":prev_qs}
  return render(request,'bview.html',context)


## 게시글 글쓰기
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    # POST방식
    id = request.session["session_id"]
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    print("bcontent : ",bcontent)
    bfile = request.FILES.get("bfile","")
    #qs = Board(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    #qs.bgroup = qs.bno
    #qs.save()
    # board저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    # bgroup 이후 입력
    qs.bgroup = qs.bno
    qs.save()
    context = {"wmsg":"1"}
    return render(request,'bwrite.html',context)

## 게시판리스트
def blist(request):
  # order_by : 정렬, -:역순정렬
  qs = Board.objects.all().order_by("-bgroup","bstep")
  print(qs.query)  # SQL 쿼리 출력
  qs = Board.objects.annotate(comment_count=Count('comment')).order_by('-bgroup', 'bstep', '-comment_count')
  
  paginator = Paginator(qs,10)           # 100개 -> 10개씩 분리작업
  nowpage = int(request.GET.get("page",1))  # 현재 몇페이지를 요청했는지 확인
  list_qs = paginator.get_page(nowpage)     # 요청된 페이지의 번호를 가져옴.
  context = {"blist":list_qs,"nowpage":nowpage}
  return render(request,'blist.html',context)
