from django.urls import path
from .views import RiskPredictionView

urlpatterns = [
    path('predict-pregnancy-risk/', RiskPredictionView.as_view(), name='predict-pregnancy-risk'),
]
