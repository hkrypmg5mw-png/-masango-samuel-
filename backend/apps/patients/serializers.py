from rest_framework import serializers
from .models import Mother, Child, Pregnancy
from apps.core.serializers import UserSerializer

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'

class PregnancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregnancy
        fields = '__all__'

class MotherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    children = ChildSerializer(many=True, read_only=True)
    pregnancies = PregnancySerializer(many=True, read_only=True)

    class Meta:
        model = Mother
        fields = '__all__'
