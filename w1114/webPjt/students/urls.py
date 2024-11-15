from django.urls import path,include
from . import views

#### 메인URL ####
app_name = 'students'
urlpatterns = [
    path('write/', views.write,name='write'),
]
