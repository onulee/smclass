from django.urls import path,include
from . import views
app_name=''   ## name:url시 사용
urlpatterns = [
    path('',views.index,name='index' ), # 메인페이지:index,main,default
]
