from django.urls import path
from .views import RiskPredictionView, HealthAssistantView

urlpatterns = [
    path('predict-risk/', RiskPredictionView.as_view(), name='predict_risk'),
    path('assistant/', HealthAssistantView.as_view(), name='health_assistant'),
]
