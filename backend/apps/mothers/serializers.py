from rest_framework import serializers, viewsets, permissions
from .models import Mother, Pregnancy
from apps.facilities.models import Facility

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class PregnancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregnancy
        fields = '__all__'

class MotherSerializer(serializers.ModelSerializer):
    user_email = serializers.EmailField(source='user.email', read_only=True)
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)
    user_last_name = serializers.CharField(source='user.last_name', read_only=True)
    pregnancies = PregnancySerializer(many=True, read_only=True)

    class Meta:
        model = Mother
        fields = '__all__'

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Mother.objects.filter(user=user)
        return Mother.objects.all()
