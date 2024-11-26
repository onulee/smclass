from django.urls import path,include
from . import views

#### 메인URL ####
app_name = 'event'
urlpatterns = [
    path('eventView/', views.eventView,name='eventView'),
]
