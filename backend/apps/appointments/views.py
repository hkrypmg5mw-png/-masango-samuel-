from rest_framework import viewsets, permissions
from .models import Appointment, ANCVisit
from .serializers import AppointmentSerializer, ANCVisitSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Appointment.objects.filter(mother__user=user)
        return Appointment.objects.all()

class ANCVisitViewSet(viewsets.ModelViewSet):
    queryset = ANCVisit.objects.all()
    serializer_class = ANCVisitSerializer
    permission_classes = [permissions.IsAuthenticated]
