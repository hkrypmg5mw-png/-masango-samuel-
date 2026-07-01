from django.db import models
from children.models import Child

class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    recommended_age_weeks = models.IntegerField()

    def __str__(self):
        return self.name

class VaccinationRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='vaccinations')
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    date_administered = models.DateField(null=True, blank=True)
    due_date = models.DateField()
    is_administered = models.BooleanField(default=False)
    administered_by = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True, blank=True)
    health_facility = models.ForeignKey('core.Facility', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.child.full_name} - {self.vaccine.name}"
