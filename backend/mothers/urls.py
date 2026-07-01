from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotherViewSet, ANCCheckupViewSet

router = DefaultRouter()
router.register(r'profiles', MotherViewSet)
router.register(r'checkups', ANCCheckupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
