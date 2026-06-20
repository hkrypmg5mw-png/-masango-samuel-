from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, ANCVisitViewSet

router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)
router.register(r'anc-visits', ANCVisitViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
