from django.db import models
from django.conf import settings

class Mother(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mother_profile')
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_name = models.CharField(max_length=255)
    emergency_contact_phone = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=5, null=True, blank=True)
    last_synced_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Mother: {self.user.get_full_name() or self.user.username}"

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    birth_weight = models.FloatField(help_text="Weight in kg")
    birth_height = models.FloatField(help_text="Height in cm")

    def __str__(self):
        return f"Child: {self.first_name} {self.last_name}"

class Pregnancy(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='pregnancies')
    start_date = models.DateField(help_text="Estimated start date / Last Menstrual Period")
    expected_delivery_date = models.DateField()
    is_active = models.BooleanField(default=True)
    risk_level = models.CharField(max_length=10, choices=(('LOW', 'Low'), ('MEDIUM', 'Medium'), ('HIGH', 'High')), default='LOW')
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Pregnancy for {self.mother} (EDD: {self.expected_delivery_date})"
