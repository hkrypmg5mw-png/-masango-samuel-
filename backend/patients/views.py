from rest_framework import viewsets, permissions
from .models import Mother, Child, Pregnancy
from .serializers import MotherSerializer, ChildSerializer, PregnancySerializer

class PatientPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        # Mothers can see their own data, health workers can see all
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['ADMIN', 'NURSE', 'DOCTOR', 'CHW']:
            return True
        if hasattr(obj, 'user'):
            return obj.user == request.user
        if hasattr(obj, 'mother'):
            return obj.mother.user == request.user
        return False

class MotherViewSet(viewsets.ModelViewSet):
    queryset = Mother.objects.all()
    serializer_class = MotherSerializer
    permission_classes = [PatientPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Mother.objects.filter(user=user)
        return Mother.objects.all()

class PregnancyViewSet(viewsets.ModelViewSet):
    queryset = Pregnancy.objects.all()
    serializer_class = PregnancySerializer
    permission_classes = [PatientPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Pregnancy.objects.filter(mother__user=user)
        return Pregnancy.objects.all()

class ChildViewSet(viewsets.ModelViewSet):
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    permission_classes = [PatientPermission]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'MOTHER':
            return Child.objects.filter(mother__user=user)
        return Child.objects.all()
