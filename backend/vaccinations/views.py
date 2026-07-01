from rest_framework import viewsets
from .models import Vaccine, VaccinationRecord
from .serializers import VaccineSerializer, VaccinationRecordSerializer

class VaccineViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer

class VaccinationRecordViewSet(viewsets.ModelViewSet):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer

    def get_queryset(self):
        if self.request.user.role == 'MOTHER':
            return VaccinationRecord.objects.filter(child__mother__user=self.request.user)
        return super().get_queryset()
