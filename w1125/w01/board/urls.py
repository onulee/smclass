from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path('blist/', views.blist, name='blist'),
    path('bwrite/', views.bwrite, name='bwrite'),
    path('bview/<str:bno>/', views.bview, name='bview'),
    path('bdelete/<str:bno>/', views.bdelete, name='bdelete'),
    path('bupdate/<str:bno>/', views.bupdate, name='bupdate'),
    path('breply/<str:bno>/', views.breply, name='breply'),
]
