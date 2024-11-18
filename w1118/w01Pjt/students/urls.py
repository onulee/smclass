from django.urls import path,include
from . import views
app_name='students'   ## name:url시 사용
urlpatterns = [
    ## 리스트
    path('list/',views.list,name='list' ), # 학생리스트
    ## 저장
    path('write/',views.write,name='write' ), # 학생입력페이지
    ## 상세
    path('<str:name>/view/',views.view,name='view' ), # 학생상세페이지 <int:no>
    ## 수정1,2,3 - 수정1
    path('<str:name>/modify/',views.modify,name='modify' ), # 학생수정1 - url
    path('modify2/',views.modify2,name='modify2' ), # 학생수정2
    path('<str:name>/modify3/',views.modify3,name='modify3' ), # 학생수정3
    ## 삭제
    path('<str:name>/delete/',views.delete,name='delete' ), # 학생삭제
    
    
    # path('doWrite/',views.doWrite,name='doWrite' ), # 학생입력페이지
]
