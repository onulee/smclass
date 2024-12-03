from django.urls import path,include
from . import views

app_name = "comment"
urlpatterns = [
    path('cwrite/', views.cwrite,name="cwrite"),
    path('cdelete/', views.cdelete,name="cdelete"),
    path('cupdate/', views.cupdate,name="cupdate"),
]


