from rest_framework import viewsets
from .models import Mother, ANCCheckup
from .serializers import MotherSerializer, ANCCheckupSerializer

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer

    def get_queryset(self):
        if self.request.user.role == 'MOTHER':
            return Mother.objects.filter(user=self.request.user)
        return super().get_queryset()

class ANCCheckupViewSet(viewsets.ModelViewSet):
    queryset = ANCCheckup.objects.all()
    serializer_class = ANCCheckupSerializer
