from rest_framework import viewsets
from .models import Appointment
from rest_framework import serializers

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def get_queryset(self):
        if self.request.user.role == 'MOTHER':
            return Appointment.objects.filter(user=self.request.user)
        elif self.request.user.role in ['NURSE', 'DOCTOR', 'CHW']:
            return Appointment.objects.filter(assigned_staff=self.request.user)
        return super().get_queryset()
