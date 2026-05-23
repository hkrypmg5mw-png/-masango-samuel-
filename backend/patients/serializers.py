from rest_framework import serializers
from .models import Mother, Child, Pregnancy
from core.serializers import UserSerializer

class MotherSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Mother
        fields = '__all__'

class PregnancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregnancy
        fields = '__all__'

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = '__all__'
