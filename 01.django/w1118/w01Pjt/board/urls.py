from django.urls import path,include
from . import views
app_name='board'   ## name:url시 사용
urlpatterns = [
    path('list/',views.list,name='list' ), 
]
