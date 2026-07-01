from rest_framework import serializers
from .models import Mother, ANCCheckup

class ANCCheckupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ANCCheckup
        fields = '__all__'

class MotherSerializer(serializers.ModelSerializer):
    anc_checkups = ANCCheckupSerializer(many=True, read_only=True)

    class Meta:
        model = Mother
        fields = '__all__'
