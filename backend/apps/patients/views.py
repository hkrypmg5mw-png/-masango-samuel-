from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Mother, Child, Pregnancy
from .serializers import MotherSerializer, ChildSerializer, PregnancySerializer
from apps.core.sync import smart_merge

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Mother.objects.filter(user=user)
        return Mother.objects.all()

    @action(detail=True, methods=['post'])
    def sync(self, request, pk=None):
        mother = self.get_object()
        local_data = request.data
        updated_instance, fields = smart_merge(local_data, mother)
        return Response({
            'status': 'synced',
            'updated_fields': fields,
            'data': MotherSerializer(updated_instance).data
        })

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Child.objects.filter(mother__user=user)
        return Child.objects.all()

class PregnancyViewSet(viewsets.ModelViewSet):
    queryset = Pregnancy.objects.all()
    serializer_class = PregnancySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Pregnancy.objects.filter(mother__user=user)
        return Pregnancy.objects.all()
