from django.urls import path,include
from . import views

app_name = 'board'
urlpatterns = [
    path('breply/<int:bno>/',views.breply,name='breply' ),  # 답변달기
    path('bdelete/<int:bno>/',views.bdelete,name='bdelete' ),  # 글삭제
    path('bmodify/<int:bno>/',views.bmodify,name='bmodify' ),  # 글수정
    path('bview/<int:bno>/',views.bview,name='bview' ),  # 글상세보기
    path('bwrite/',views.bwrite,name='bwrite' ),         # 글쓰기
    path('blist/',views.blist,name='blist' ),            # 게시판리스트  
]
