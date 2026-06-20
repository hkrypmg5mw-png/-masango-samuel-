from django.db import models
from apps.patients.models import Child

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    recommended_age_weeks = models.IntegerField()

    def __str__(self):
        return self.name

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_administered = models.DateField()
    administered_by = models.ForeignKey('core.User', on_delete=models.SET_NULL, null=True)
    batch_number = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.vaccine.name} for {self.child.first_name}"
