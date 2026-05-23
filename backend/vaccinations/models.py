from django.db import models
from patients.models import Child
from appointments.models import Appointment

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    recommended_age_days = models.IntegerField() # Days from birth

    def __str__(self):
        return self.name

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    appointment = models.OneToOneField(Appointment, on_delete=models.SET_NULL, null=True, blank=True)
    date_administered = models.DateField(null=True, blank=True)
    administered_by = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('MISSED', 'Missed')), default='PENDING')

    def __str__(self):
        return f"{self.vaccine.name} for {self.child}"
