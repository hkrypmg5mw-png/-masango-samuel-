from django.db import models
from django.conf import settings

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100) # e.g., Hospital, Health Center, Clinic

    def __str__(self):
        return self.name

class Mother(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mother_profile')
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    assigned_facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, related_name='mothers')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Pregnancy(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='pregnancies')
    start_date = models.DateField()
    expected_delivery_date = models.DateField()
    status = models.CharField(max_length=20, choices=[('ONGOING', 'Ongoing'), ('COMPLETED', 'Completed'), ('COMPLICATED', 'Complicated')], default='ONGOING')
    is_high_risk = models.BooleanField(default=False)
    risk_notes = models.TextField(blank=True)

    def __str__(self):
        return f"Pregnancy of {self.mother} - EDD: {self.expected_delivery_date}"
