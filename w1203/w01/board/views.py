from django.shortcuts import render
from board.models import Board
from member.models import Member
from comment.models import Comment
from django.http import JsonResponse,HttpResponse
## 게시글저장
## 1,aaa 2,aaa 3,bbb 4,aaa

## 좋아요. board,member  3번게시글 aaa, 3번 bbb, 1번게시글 aaa
def likes(request):
  id = request.session["session_id"]
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno")
  board = Board.objects.get(bno=bno)
  
  # 저장 board.bno, board.member.id
  if board.like_members.filter(pk=id).exists(): # 좋아요클릭을 했으면
    board.like_members.remove(member)
    result = "remove" # 좋아요취소
  else:
    board.like_members.add(member)
    result = "add"    # 좋아요추가  
  
  print("좋아요 개수 확인 : ",board.like_members.count())
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


## 상세보기
def bview(request,bno):
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  
  qs = Board.objects.filter(bno=bno)
  
  ##
  # 저장 board.bno, board.member.id
  if qs[0].like_members.filter(pk=id).exists(): # 좋아요클릭을 했으면
    result = "1"
    print("result : ",result) 
  else:
    result = "0"
    print("result : ",result) 
  count = qs[0].like_members.count() 
  
  
  # 하단댓글가져오기
  c_qs = Comment.objects.filter(board=qs[0]).order_by("-cno")
  print("확인 : ",c_qs,c_qs.count)
  context = {"board":qs[0],"clist":c_qs,"result":result,"count":count}
  return render(request,'bview.html',context)


## 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
