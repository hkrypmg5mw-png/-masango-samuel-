from django.db import models

class Facility(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    facility_type = models.CharField(max_length=100, choices=(
        ('HOSPITAL', 'Hospital'),
        ('CLINIC', 'Clinic'),
        ('HEALTH_CENTER', 'Integrated Health Center'),
    ))

    def __str__(self):
        return self.name

class AuditLog(models.Model):
    user = models.ForeignKey('authentication.User', on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.action} at {self.timestamp}"
