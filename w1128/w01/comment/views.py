from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse,HttpResponse
from django.core import serializers # json타입
from member.models import Member
from board.models import Board
from comment.models import Comment
from django.core import serializers 

# 하단댓글쓰기저장
def cwrite(request):
  # 데이터가져오기
  id = request.session['session_id']
  member = Member.objects.get(id=id)
  bno = request.POST.get("bno",1)
  board = Board.objects.get(bno=bno)
  cpw = request.POST.get("pw","")
  ccontent = request.POST.get("ccontent","")
  print(cpw,ccontent) ## 성공
  # 데이터저장
  qs = Comment.objects.create(board=board,member=member,cpw=cpw,ccontent=ccontent) 
  print("cno : ",qs.cno)
  list_qs = list(Comment.objects.filter(cno=qs.cno).values())
  print(list_qs)
  context = {"comment":list_qs,"result":"success"}
  
  return JsonResponse(context)


# 하단댓글리스트
def clist(request):
  return
