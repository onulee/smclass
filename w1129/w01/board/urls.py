from django.urls import path,include
from . import views

app_name = "board"
urlpatterns = [
    path('map/', views.map,name="map"),
    path('blist/', views.blist,name="blist"),
    path('likes/', views.likes,name="likes"),
    path('form/', views.form,name="form"),
    path('bview/<int:bno>/', views.bview,name="bview"),
]


