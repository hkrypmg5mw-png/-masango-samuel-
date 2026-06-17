from django.db import models
from django.conf import settings
from apps.children.models import Child

class Vaccine(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    recommended_age_weeks = models.IntegerField()

    def __str__(self):
        return self.name

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_administered = models.DateField()
    administered_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    facility = models.ForeignKey('facilities.Facility', on_delete=models.SET_NULL, null=True)
    next_dose_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.vaccine.name} for {self.child} on {self.date_administered}"
