from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VaccineViewSet, VaccinationRecordViewSet

router = DefaultRouter()
router.register(r'vaccines', VaccineViewSet)
router.register(r'records', VaccinationRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
