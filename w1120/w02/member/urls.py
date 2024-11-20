from django.urls import path,include
from . import views

app_name = 'member'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('mlist/', views.mlist, name='mlist'),
    path('cookWrite/', views.cookWrite, name='cookWrite'),
    path('cookDelete/', views.cookDelete, name='cookDelete'),
]
