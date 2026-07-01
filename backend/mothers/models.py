from django.db import models
from django.conf import settings

class Mother(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mother_profile')
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    last_menstrual_period = models.DateField(null=True, blank=True)
    estimated_date_of_delivery = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=5, blank=True)
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=15)
    risk_level = models.CharField(max_length=20, choices=(
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
    ), default='LOW')

    def __str__(self):
        return self.full_name

class ANCCheckup(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='anc_checkups')
    visit_date = models.DateField()
    gestational_age_weeks = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    systolic_bp = models.IntegerField()
    diastolic_bp = models.IntegerField()
    fetal_heart_rate = models.IntegerField(null=True, blank=True)
    notes = models.TextField(blank=True)
    nurse_notes = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.mother.full_name} - Week {self.gestational_age_weeks}"
