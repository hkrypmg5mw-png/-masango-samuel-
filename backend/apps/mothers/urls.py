from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotherViewSet, PregnancyViewSet

router = DefaultRouter()
router.register(r'mothers', MotherViewSet)
router.register(r'pregnancies', PregnancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
