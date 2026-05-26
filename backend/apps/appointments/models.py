from django.db import models
from apps.patients.models import Mother, Child
from django.conf import settings

class Appointment(models.Model):
    TYPE_CHOICES = (
        ('ANC', 'Antenatal Care'),
        ('PNC', 'Postnatal Care'),
        ('VACCINATION', 'Vaccination'),
        ('GENERAL', 'General Checkup'),
    )
    STATUS_CHOICES = (
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('MISSED', 'Missed'),
        ('CANCELLED', 'Cancelled'),
    )
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, null=True, blank=True)
    child = models.ForeignKey(Child, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField()
    appointment_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    notes = models.TextField(null=True, blank=True)
    health_worker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, limit_choices_to={'role__in': ['NURSE', 'DOCTOR', 'CHW']})

    def __str__(self):
        return f"{self.appointment_type} on {self.date}"

class ANCVisit(models.Model):
    pregnancy = models.ForeignKey('patients.Pregnancy', on_delete=models.CASCADE, related_name='anc_visits')
    visit_date = models.DateField()
    weight = models.FloatField(help_text="Weight in kg")
    bp_systolic = models.IntegerField()
    bp_diastolic = models.IntegerField()
    fundal_height = models.FloatField(null=True, blank=True)
    fetal_heart_rate = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"ANC Visit for {self.pregnancy} on {self.visit_date}"
