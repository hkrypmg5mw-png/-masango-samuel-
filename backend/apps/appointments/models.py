from django.db import models
from django.conf import settings
from apps.mothers.models import Mother, Pregnancy, Facility

class Appointment(models.Model):
    class Type(models.TextChoices):
        ANC = 'ANC', 'Antenatal Care'
        PNC = 'PNC', 'Postnatal Care'
        VACCINATION = 'VACCINATION', 'Vaccination'
        GENERAL = 'GENERAL', 'General Consultation'

    class Status(models.TextChoices):
        SCHEDULED = 'SCHEDULED', 'Scheduled'
        COMPLETED = 'COMPLETED', 'Completed'
        MISSED = 'MISSED', 'Missed'
        CANCELLED = 'CANCELLED', 'Cancelled'

    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='appointments')
    pregnancy = models.ForeignKey(Pregnancy, on_delete=models.SET_NULL, null=True, blank=True)
    appointment_type = models.CharField(max_length=20, choices=Type.choices)
    date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SCHEDULED)
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True)
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.appointment_type} for {self.mother} on {self.date}"

class ANCVisit(models.Model):
    appointment = models.OneToOneField(Appointment, on_delete=models.CASCADE, related_name='anc_visit_details')
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    fundal_height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    fetal_heart_rate = models.IntegerField(null=True, blank=True)
    hemoglobin = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"ANC Visit Details for {self.appointment}"
