from django.urls import path,include
from . import views

#### 메인URL ####
app_name = ''
urlpatterns = [
    path('', views.index,name='index'),
]
