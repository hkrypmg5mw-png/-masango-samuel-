from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    body = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    notification_type = models.CharField(max_length=50, choices=(
        ('APPOINTMENT', 'Appointment Reminder'),
        ('VACCINATION', 'Vaccination Reminder'),
        ('RISK_ALERT', 'High Risk Alert'),
        ('SYSTEM', 'System Message'),
        ('SOS', 'Emergency SOS'),
    ))

    def __str__(self):
        return f"{self.title} for {self.user}"

class SOSAlert(models.Model):
    mother = models.ForeignKey('patients.Mother', on_delete=models.CASCADE)
    location_lat = models.FloatField(null=True, blank=True)
    location_lng = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='PENDING') # PENDING, RESPONDED, RESOLVED

    def __str__(self):
        return f"SOS from {self.mother} at {self.timestamp}"
