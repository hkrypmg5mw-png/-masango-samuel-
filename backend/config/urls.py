from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MCH Follow-Up System API",
      default_version='v1',
      description="API for Maternal and Child Health Follow-Up System (Cameroon)",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/mothers/', include('mothers.urls')),
    path('api/children/', include('children.urls')),
    path('api/appointments/', include('appointments.urls')),
    path('api/vaccinations/', include('vaccinations.urls')),
    path('api/notifications/', include('notifications.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/ai/', include('ai.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
