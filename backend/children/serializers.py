from rest_framework import serializers
from .models import Child, GrowthRecord

class GrowthRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrowthRecord
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    growth_records = GrowthRecordSerializer(many=True, read_only=True)

    class Meta:
        model = Child
        fields = '__all__'
