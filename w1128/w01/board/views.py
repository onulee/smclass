from django.shortcuts import render
from board.models import Board
from comment.models import Comment

## 상세보기
def bview(request,bno):
  qs = Board.objects.filter(bno=bno)
  board = Board.objects.get(bno=bno)
  c_qs = Comment.objects.filter(board=board).order_by("-cno")
  context = {"board":qs[0], "comment":c_qs}
  return render(request,'bview.html',context)

## 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
