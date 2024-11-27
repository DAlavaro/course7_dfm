# config/urls.py
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', include('app.courses.urls')),
    path('lessons/', include('app.lessons.urls')),
    path('users/', include('app.users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
