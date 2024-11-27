from django.contrib import admin
from django.urls import path,include
from . import views

app_name="member"
urlpatterns = [
    path('join01/', views.join01,name='join01' ),
    path('join02/', views.join02,name='join02' ),
    path('idChk/', views.idChk,name='idChk' ),
    path('login/', views.login,name='login' ),
    path('loginChk/', views.loginChk,name='loginChk' ),
]

