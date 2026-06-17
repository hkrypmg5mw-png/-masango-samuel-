from django.db import models
from apps.mothers.models import Mother

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='children')
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=[('MALE', 'Male'), ('FEMALE', 'Female')])
    birth_weight = models.DecimalField(max_digits=5, decimal_places=2, help_text="Weight in kg")
    birth_height = models.DecimalField(max_digits=5, decimal_places=2, help_text="Height in cm")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class GrowthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='growth_records')
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    muac = models.DecimalField(max_digits=5, decimal_places=2, help_text="Mid-Upper Arm Circumference", null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Growth Record for {self.child} on {self.date}"
