from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path('location/', views.location,name="location"),
    path('likes/', views.likes,name="likes"),
    path('blist/', views.blist,name="blist"),
    path('form/', views.form,name="form"),
    path('bview/<int:bno>/', views.bview,name="bview"),
]


