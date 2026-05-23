from django.db import models
from patients.models import Mother, Pregnancy, Child
from django.conf import settings

class Appointment(models.Model):
    APPOINTMENT_TYPES = (
        ('ANC', 'Antenatal Care'),
        ('PNC', 'Postnatal Care'),
        ('IMMUNIZATION', 'Immunization'),
        ('GENERAL', 'General Follow-up'),
    )
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, blank=True)
    health_worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    appointment_date = models.DateTimeField()
    appointment_type = models.CharField(max_length=20, choices=APPOINTMENT_TYPES)
    status = models.CharField(max_length=20, choices=(('SCHEDULED', 'Scheduled'), ('COMPLETED', 'Completed'), ('MISSED', 'Missed'), ('CANCELLED', 'Cancelled')), default='SCHEDULED')
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.appointment_type} on {self.appointment_date}"

class ANCVisit(models.Model):
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.CASCADE, related_name='anc_visits')
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE)
    visit_date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    fetal_heart_rate = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"ANC Visit for {self.pregnancy.mother} on {self.visit_date}"
