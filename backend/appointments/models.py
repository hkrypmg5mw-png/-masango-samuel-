from django.db import models
from django.conf import settings

class Appointment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments')
    assigned_staff = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='staff_appointments')
    date = models.DateTimeField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=(
        ('SCHEDULED', 'Scheduled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
        ('MISSED', 'Missed'),
    ), default='SCHEDULED')
    facility = models.ForeignKey('core.Facility', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title} for {self.user.phone_number}"
