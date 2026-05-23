from datetime import date
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import RiskAssessment
from .serializers import RiskAssessmentSerializer
from .predictor.risk_predictor import RiskPredictor
from patients.models import Pregnancy, Child
from appointments.models import Appointment

class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=False, methods=['post'], url_path='predict-pregnancy')
    def predict_pregnancy(self, request):
        pregnancy_id = request.data.get('pregnancy_id')
        try:
            pregnancy = Pregnancy.objects.get(id=pregnancy_id)
            mother = pregnancy.mother

            # Calculate age from mother's date_of_birth
            today = date.today()
            age = today.year - mother.date_of_birth.year - ((today.month, today.day) < (mother.date_of_birth.month, mother.date_of_birth.day))

            # Simplified: Use latest ANC visit or default values
            latest_visit = pregnancy.anc_visits.order_by('-visit_date').first()
            systolic = latest_visit.blood_pressure_systolic if latest_visit else 120
            diastolic = latest_visit.blood_pressure_diastolic if latest_visit else 80

            predictor = RiskPredictor()
            label, score = predictor.predict_pregnancy_risk(
                age=age,
                systolic=systolic,
                diastolic=diastolic,
                prev_complications=bool(pregnancy.previous_complications)
            )

            assessment = RiskAssessment.objects.create(
                mother=pregnancy.mother,
                pregnancy=pregnancy,
                assessment_type='PREGNANCY',
                risk_score=score,
                risk_label=label,
                recommendations=f"Automated risk assessment: {label}"
            )
            return Response(RiskAssessmentSerializer(assessment).data)
        except Pregnancy.DoesNotExist:
            return Response({'error': 'Pregnancy not found'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=False, methods=['post'], url_path='predict-appointment')
    def predict_appointment(self, request):
        appointment_id = request.data.get('appointment_id')
        try:
            appointment = Appointment.objects.get(id=appointment_id)
            predictor = RiskPredictor()
            # Simplified features
            label, score = predictor.predict_appointment_risk(0, 5.0, 25)

            assessment = RiskAssessment.objects.create(
                mother=appointment.mother,
                child=appointment.child,
                assessment_type='APPOINTMENT',
                risk_score=score,
                risk_label=label,
                recommendations=f"Likelihood of missing: {label}"
            )
            return Response(RiskAssessmentSerializer(assessment).data)
        except Appointment.DoesNotExist:
            return Response({'error': 'Appointment not found'}, status=status.HTTP_404_NOT_FOUND)
