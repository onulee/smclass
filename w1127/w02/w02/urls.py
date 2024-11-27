from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls') ),
    path('member/',include('member.urls') ),
]


## settins.py 안에 파일 있는데
# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
