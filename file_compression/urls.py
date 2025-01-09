from django.contrib import admin
from django.urls import path
from compressor import views  # Import views directly
from django.conf import settings
from django.conf.urls.static import static # Import views directly

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.upload_file, name='upload_file'),  # Single route for file upload
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
