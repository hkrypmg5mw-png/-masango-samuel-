from rest_framework import viewsets
from .models import AppNotification, SMSNotification
from .serializers import AppNotificationSerializer, SMSNotificationSerializer

class AppNotificationViewSet(viewsets.ModelViewSet):
    queryset = AppNotification.objects.all()
    serializer_class = AppNotificationSerializer

    def get_queryset(self):
        return AppNotification.objects.filter(user=self.request.user)

class SMSNotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SMSNotification.objects.all()
    serializer_class = SMSNotificationSerializer
