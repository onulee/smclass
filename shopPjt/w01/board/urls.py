from django.urls import path,include
from . import views

app_name= 'board'
urlpatterns = [
    
    path('like/', views.like, name="like"),
    path('blist/', views.blist, name="blist"), #blist 함수연결
    path('bwrite/', views.bwrite, name="bwrite"), #bwrite 함수연결
    path('bview/<int:bno>/', views.bview, name="bview"), #blist 함수연결
    path('bdelete/<int:bno>/', views.bdelete, name="bdelete"), #bdelete 함수연결
    path('bupdate/<int:bno>/', views.bupdate, name="bupdate"), #bupdate 함수연결
    path('breply/<int:bno>/', views.breply, name="breply"), #breply 함수연결
]
