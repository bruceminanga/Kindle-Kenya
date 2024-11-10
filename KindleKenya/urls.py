from django.contrib import admin
from django.urls import path, include

# serving media files
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app1.urls", namespace="app1")),
]

# serving media files eg images
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
