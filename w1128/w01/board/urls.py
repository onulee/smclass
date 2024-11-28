from django.urls import path,include
from . import views

app_name="board"
urlpatterns = [
    path('blist/', views.blist,name="blist"),
    path('bview/<int:bno>/', views.bview,name="bview"),
]
