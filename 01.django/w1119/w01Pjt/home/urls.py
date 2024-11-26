from django.urls import path,include 
from . import views
# http://127.0.0.1:8000/
app_name= ''
urlpatterns = [
    path('',views.index,name='index' ), 
]
