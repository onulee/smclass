from django.contrib import admin
from django.urls import path,include #include추가
urlpatterns = [
    path('admin/', admin.site.urls), #admin관리자사이트 연결
    path('students/', include('students.urls')), #students > urls.py연결
    path('', include('home.urls')), #home > urls.py연결
]
