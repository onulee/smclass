from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board
from member.models import Member
from comment.models import Comment



# 3. 댓글수정저장
def csave(request):
  cno = request.POST.get("cno")
  ccontent = request.POST.get("ccontent")
  print("ccontent :",ccontent)
  # get 방식
  # qs = Comment.objects.get(cno=cno)
  # qs.ccontent = ccontent
  # qs.update()

  #filter 방식
  qs = Comment.objects.filter(cno=cno)
  qs.update(ccontent=ccontent)
  j_qs = list(qs.values())

  context = {"result":"success","comment":j_qs}
  print("j_qs : ",j_qs)
  return JsonResponse(context)

# 2. 댓글삭제
def cdelete(request):
  cno = request.POST.get("cno")
  Comment.objects.get(cno=cno).delete() 
  print("cdelete cno : ",cno)
  context = {"result":"success"}
  return JsonResponse(context)


# 1. 댓글저장
def cwrite(request):
  bno = request.POST.get("bno")
  board = Board.objects.get(bno=bno)
  id = request.session["session_id"]
  member = Member.objects.get(id=id)
  cpw = request.POST.get("cpw")
  ccontent = request.POST.get("ccontent")
  print("cpw,ccontent :",cpw,ccontent)
  qs = Comment.objects.create(board=board,member=member,cpw=cpw,ccontent=ccontent)
  j_qs = list(Comment.objects.filter(cno=qs.cno).values())

  context = {"result":"success","comment":j_qs}
  print("j_qs : ",j_qs)
  return JsonResponse(context)

# 댓글전체리스트
def clist(request):
  context = {}
  return JsonResponse(context)