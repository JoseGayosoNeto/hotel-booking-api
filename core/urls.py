from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/docs/', SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-doc'),
    path('api/v1/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('api/v1/', include('roles.urls')),
    path('api/v1/', include('room_services.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
