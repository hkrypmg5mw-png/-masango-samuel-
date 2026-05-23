from django.db import models
from patients.models import Mother, Child, Pregnancy

class RiskAssessment(models.Model):
    ASSESSMENT_TYPES = (
        ('PREGNANCY', 'Pregnancy Risk'),
        ('CHILD', 'Child Health Risk'),
        ('APPOINTMENT', 'Missed Appointment Risk'),
    )
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, blank=True)
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, null=True, blank=True)
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPES)
    risk_score = models.FloatField() # 0.0 to 1.0
    risk_label = models.CharField(max_length=20) # LOW, MEDIUM, HIGH
    recommendations = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.assessment_type} - {self.risk_label} ({self.created_at})"
