from django.db import models
from django.conf import settings

class Mother(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mother_profile')
    date_of_birth = models.DateField()
    address = models.TextField()
    emergency_contact_number = models.CharField(max_length=15)
    blood_group = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Pregnancy(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='pregnancies')
    start_date = models.DateField()
    expected_due_date = models.DateField()
    is_active = models.BooleanField(default=True)
    previous_complications = models.TextField(blank=True, null=True)
    risk_level = models.CharField(max_length=20, default='LOW') # LOW, MEDIUM, HIGH

    def __str__(self):
        return f"Pregnancy of {self.mother} (Due: {self.expected_due_date})"

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    birth_weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
