
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls')), #home 연결
    path('member/',include('member.urls')), #member 연결
    path('board/',include('board.urls')), 
    path('comment/',include('comment.urls')), 
]
# media연결
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)