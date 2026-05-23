from rest_framework import serializers
from .models import Appointment, ANCVisit

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class ANCVisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ANCVisit
        fields = '__all__'
