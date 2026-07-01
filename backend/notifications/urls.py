from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppNotificationViewSet, SMSNotificationViewSet

router = DefaultRouter()
router.register(r'app', AppNotificationViewSet)
router.register(r'sms', SMSNotificationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
