from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')), #urls추가
    path('students/', include('students.urls')), #urls추가
    path('board/', include('board.urls')), #urls추가
]
