from django.urls import path,include
from . import views

app_name='member'
urlpatterns = [
    ## 회원정보관련
    path('mdelete/<str:id>/', views.mdelete, name='mdelete'), # 회원정보삭제
    path('mwrite/', views.mwrite, name='mwrite'), # 회원정보입력
    path('mupdate/<str:id>/', views.mupdate, name='mupdate'), # 회원정보수정
    path('mview/<str:id>/', views.mview, name='mview'), # 회원상세
    path('mlist/', views.mlist, name='mlist'), # 회원리스트
    
    ## 로그인관련
    path('login/', views.login, name='login'), # 로그인
    path('logout/', views.logout, name='logout'), #로그아웃
]
