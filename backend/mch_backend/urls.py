from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UserViewSet, FacilityViewSet
from patients.views import MotherViewSet, PregnancyViewSet, ChildViewSet
from appointments.views import AppointmentViewSet, ANCVisitViewSet
from vaccinations.views import VaccineViewSet, VaccinationRecordViewSet
from ml.views import RiskAssessmentViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'mothers', MotherViewSet)
router.register(r'pregnancies', PregnancyViewSet)
router.register(r'children', ChildViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'anc-visits', ANCVisitViewSet)
router.register(r'vaccines', VaccineViewSet)
router.register(r'vaccination-records', VaccinationRecordViewSet)
router.register(r'risk-assessments', RiskAssessmentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
