from django.shortcuts import render
from board.models import Board
from member.models import Member
from comment.models import Comment
from django.db.models import F,Q
from django.core.paginator import Paginator
from django.http import JsonResponse
import requests
from django.conf import settings


# 2. 카카오페이 결제 준비 API 호출
def prepare_payment(request):
  KAKAO_PAY_KEY='3d520f84162912f2e93a00ba52dd1367'
  KAKAO_PAY_CID='TC0ONETIME'
  KAKAOPAY_BASE_URL = 'https://kapi.kakao.com/v1/payment/ready'
  url = KAKAOPAY_BASE_URL
    
  headers = {
      "Authorization": f"KakaoAK {KAKAO_PAY_KEY}",
      "Content-Type": "application/json",
  }
  data = {
      "cid": "TC0ONETIME",  # 테스트용 CID
      "partner_order_id": "1234567890",
      "partner_user_id": "test_user",
      "item_name": "초코파이",
      "quantity": 1,
      "total_amount": 1000,
      "vat_amount": 100,
      "tax_free_amount": 0,
      "approval_url": "http://127.0.0.1/payment/approval",
      "cancel_url": "http://127.0.0.1/payment/cancel",
      "fail_url": "http://127.0.0.1/payment/fail",
  }
  response = requests.post(url, headers=headers, data=data)
  result = response.json()
  
  print("결과 : ",result)

  if response.status_code == 200:
      return JsonResponse({"next_redirect_pc_url": result["next_redirect_pc_url"]})
  else:
      return JsonResponse({"error": result}, status=400)
  


# 1. 카카오페이 연결을 위한 페이지
def kakaopay(request):
  return render(request,"kakaopay.html")


# 좋아요
def like(request):
  bno = request.POST.get("bno")
  print("bno : ",bno)
  board = Board.objects.get(bno=bno)
  id = request.session['session_id']
  member = Member.objects.get(id=id)

  # 좋아요를 했던 회원인지 확인
  if board.like_members.filter(pk=id).exists():
    result = 0
    board.like_members.remove(member) #좋아요를 했던 회원은 삭제
  else:
    result = 1
    board.like_members.add(member)  # 좋아요를 하지 않았던 회원은 추가
  context = {"result":result,"count":board.like_members.count()}
  print("count : ",board.like_members.count())
  return JsonResponse(context)



##답글달기
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
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")

    # 검색 2가지
    # Board.objects.get(bno=bno)
    # qs.save()
    # Board.objects.filter(bno=bno) 여러개 가능
    # update()

    # 부모보다 큰 bstep 1증가
    qs = Board.objects.filter(bgroup = bgroup, bstep__gt = bstep) # bstep > bstep
    qs.update(bstep = F("bstep")+1)

    Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1,bfile=bfile)
    context = {"rmsg":"1","nowpage":nowpage}
    return render(request,'breply.html',context)


##게시글 수정
def bupdate(request,bno):
  if request.method == "GET":
    nowpage = request.GET.get("page",1)
    qs = Board.objects.get(bno=bno)
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


##게시글 삭제
def bdelete(request,bno):
  qs = Board.objects.get(bno=bno)
  qs.delete()
  context = {"dmsg":bno}
  return render(request,'blist.html',context)


##게시글 작성
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    # POST방식
    id = request.session["session_id"]
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    bfile = request.FILES.get("bfile","")
    # board 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    # bgroup 이후 입력
    qs.bgroup = qs.bno
    qs.save()
    context = {"wmsg":"1"}
    return render(request,'bwrite.html',context)

##게시글 상세보기
def bview(request,bno):
  nowpage = request.POST.get("page",1)
  qs = Board.objects.get(bno=bno) # 현재글
  qs.bhit = qs.bhit + 1
  qs.save()

  #하단 댓글 가져오기
  c_qs = Comment.objects.filter(board=qs).order_by("-cno")
  print("c_qs",c_qs)

  next_qs = Board.objects.filter(Q(bgroup__gt=qs.bgroup,bstep__gte=qs.bstep)|\
                                 Q(bgroup=qs.bgroup,bstep__lt=qs.bstep)).order_by("-bgroup","bstep").last()
  prev_qs = Board.objects.filter(Q(bgroup__lt=qs.bgroup,bstep__lte=qs.bstep)|\
                                 Q(bgroup=qs.bgroup,bstep__gt=qs.bstep)).order_by("-bgroup","bstep").first()
  nowpage = request.GET.get("page")
  print("이전글 :",prev_qs.bno)
  context={"board":qs,"nowpage":nowpage,"next_board":next_qs,"prev_board":prev_qs,"clist":c_qs}
  return render(request,'bview.html',context)



## 게시판리스트
def blist(request):
  # order_by : 정렬, -:역순정렬
  qs = Board.objects.all().order_by("-bgroup","bstep")
  paginator = Paginator(qs,10) # 100개 -> 10개씩 분리작업
  nowpage = int(request.GET.get("page",1))  # 현재 몇페이지를 요청했는지 확인
  list_qs = paginator.get_page(nowpage)  # 요청된 페이지의 번호를 가져옴

  context = {"blist":list_qs,"nowpage":nowpage}
  return render(request,'blist.html',context)