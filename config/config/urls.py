from django.contrib import admin
from django.urls import path

from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from music.views import MusicAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MusicAPIView.as_view(), name='all_music'),
    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
