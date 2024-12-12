from django.urls import path,include
from . import views

app_name= 'payment'
urlpatterns = [
    path('approval/', views.approval, name="approval"), 
    path('cancel/', views.cancel, name="cancel"), 
    path('fail/', views.fail, name="fail"), 
    
]

