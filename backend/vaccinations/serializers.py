from rest_framework import serializers
from .models import Vaccine, VaccinationRecord

class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = '__all__'

class VaccinationRecordSerializer(serializers.ModelSerializer):
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')

    class Meta:
        model = VaccinationRecord
        fields = '__all__'
