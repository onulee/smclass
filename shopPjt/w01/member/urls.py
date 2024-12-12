from django.urls import path,include
from . import views

app_name= 'member'
urlpatterns = [
    path('login/', views.login, name="login"), #login 함수연결
    path('logout/', views.logout, name="logout"), #logout 함수연결
]
