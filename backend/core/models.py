from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('MOTHER', 'Mother'),
        ('NURSE', 'Nurse'),
        ('DOCTOR', 'Doctor'),
        ('CHW', 'Community Health Worker'),
        ('ADMIN', 'Administrator'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='MOTHER')
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    facility = models.ForeignKey('Facility', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100) # e.g., Clinic, Hospital, Health Center

    def __str__(self):
        return self.name
