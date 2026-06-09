from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.authentication.urls')),
    path('api/mothers/', include('apps.mothers.urls')),
    path('api/children/', include('apps.children.urls')),
    path('api/appointments/', include('apps.appointments.urls')),
    path('api/vaccinations/', include('apps.vaccinations.urls')),
    path('api/facilities/', include('apps.facilities.urls')),
    path('api/ai/', include('apps.ai.urls')),
]
