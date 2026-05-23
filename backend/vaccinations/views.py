from rest_framework import viewsets, permissions
from .models import Vaccine, VaccinationRecord
from .serializers import VaccineSerializer, VaccinationRecordSerializer

class VaccineViewSet(viewsets.ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = [permissions.IsAuthenticated]

class VaccinationRecordViewSet(viewsets.ModelViewSet):
    queryset = VaccinationRecord.objects.all()
    serializer_class = VaccinationRecordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return VaccinationRecord.objects.filter(child__mother__user=user)
        return VaccinationRecord.objects.all()
