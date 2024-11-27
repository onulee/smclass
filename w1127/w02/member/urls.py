from django.contrib import admin
from django.urls import path,include
from . import views

app_name="member"
urlpatterns = [
    path('login/', views.login,name='login' ),
    #/member/loginChk/
    path('loginChk/', views.loginChk,name='loginChk' ),
]

