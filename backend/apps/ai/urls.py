from django.urls import path
from .views import MaternalRiskPredictionView, ChildRiskPredictionView, AIHealthAssistantView

urlpatterns = [
    path('predict/maternal/', MaternalRiskPredictionView.as_view(), name='predict-maternal'),
    path('predict/child/', ChildRiskPredictionView.as_view(), name='predict-child'),
    path('assistant/', AIHealthAssistantView.as_view(), name='ai-assistant'),
]
