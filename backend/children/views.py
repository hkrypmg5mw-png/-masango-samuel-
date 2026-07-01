from rest_framework import viewsets
from .models import Child, GrowthRecord
from .serializers import ChildSerializer, GrowthRecordSerializer

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer

    def get_queryset(self):
        if self.request.user.role == 'MOTHER':
            return Child.objects.filter(mother__user=self.request.user)
        return super().get_queryset()

class GrowthRecordViewSet(viewsets.ModelViewSet):
    queryset = GrowthRecord.objects.all()
    serializer_class = GrowthRecordSerializer
