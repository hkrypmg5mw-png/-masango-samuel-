from django.urls import path
from .views import AIAssistantView

urlpatterns = [
    path('ask/', AIAssistantView.as_view(), name='ai_ask'),
]
