from django.shortcuts import render,redirect
from board.models import Board
from django.db.models import Max
from django.contrib import messages
from django.db.models import F

# 글수정페이지, 글수정저장
def bmodify(request,bno):
  print("게시글 번호 : ",bno)
  if request.method == "GET":
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request,'bmodify.html',context)
  else: #post
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect("board:blist")
    return render(request,'bmodify.html',{'u_msg':bno})

# 글상세보기
def bview(request,bno):
  print("게시글 번호 : ",bno)
  
  # 조회수 1증가 - get : save()
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {'board':qs}
  
  # 조회수 1증가 - filter : update()
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit=F('bhit') + 1)
  context = {'board':qs[0]}
    
  return render(request,'bview.html',context)



# 글쓰기페이지, 글쓰기저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1
    # 오라클 sequence.nextval, sequence.currval
    # bno,bstep,bindent,bhit,bdate - 자동  
    # id,btitle,bcontent,bgroup - 입력
    
    # DB저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # 1회 노출
    messages.success(request,message='게시글이 저장되었습니다.')
    # return redirect('board:blist')
    return render(request,'bwrite.html',{'w_msg':'1'})
    

# 게시판리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)
