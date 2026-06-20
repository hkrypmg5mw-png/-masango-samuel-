from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MotherViewSet, ChildViewSet, PregnancyViewSet

router = DefaultRouter()
router.register(r'mothers', MotherViewSet)
router.register(r'children', ChildViewSet)
router.register(r'pregnancies', PregnancyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
