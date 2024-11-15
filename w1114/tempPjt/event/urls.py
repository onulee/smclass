from django.urls import path,include
from . import views

app_name = 'event'
urlpatterns = [
    path('eventView/',views.eventView,name='eventView'),
]
