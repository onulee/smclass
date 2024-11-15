from django.contrib import admin
from django.urls import path,include

#### 메인URL ####

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),
    path('event/', include('event.urls')),
    path('', include('home.urls')),
]
