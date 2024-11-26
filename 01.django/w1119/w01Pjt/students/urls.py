from django.urls import path,include #include추가
from . import views
app_name = 'students' #app_name설정
urlpatterns = [
         # url링크, views함수호출, name링크
    path('write/',views.write,name='write' ), 
    path('search/',views.search,name='search' ),  #검색
    path('list/',views.list,name='list' ), 
    path('view/<str:name>/',views.view,name='view' ), 
    path('update/',views.update,name='update' ), # 파라미터 형태
    path('delete/<str:name>/',views.delete,name='delete' ), 
    # path('update/<str:name>/',views.update,name='update' ), 
]
