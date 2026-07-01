from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ChildViewSet, GrowthRecordViewSet

router = DefaultRouter()
router.register(r'list', ChildViewSet)
router.register(r'growth', GrowthRecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
