from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100) # e.g., Hospital, Health Center, Clinic

    def __str__(self):
        return self.name
