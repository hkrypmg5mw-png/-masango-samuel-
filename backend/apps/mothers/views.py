from rest_framework import viewsets
from .models import Mother, Pregnancy
from .serializers import MotherSerializer, PregnancySerializer

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Mother.objects.filter(user=user)
        return Mother.objects.all()

class PregnancyViewSet(viewsets.ModelViewSet):
    queryset = Pregnancy.objects.all()
    serializer_class = PregnancySerializer

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Pregnancy.objects.filter(mother__user=user)
        return Pregnancy.objects.all()
