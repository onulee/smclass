from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('member/', include('member.urls')),
    path('board/', include('board.urls')),
]

# 이미지등록url 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
