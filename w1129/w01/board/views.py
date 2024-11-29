from django.shortcuts import render
from board.models import Board
from comment.models import Comment
from django.http import HttpResponse 

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
  qs = Board.objects.filter(bno=bno)
  # 하단댓글가져오기
  c_qs = Comment.objects.filter(board=qs[0]).order_by("-cno")
  print("확인 : ",c_qs,c_qs.count)
  context = {"board":qs[0],"clist":c_qs}
  return render(request,'bview.html',context)


## 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
