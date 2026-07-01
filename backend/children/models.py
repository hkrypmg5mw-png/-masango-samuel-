from django.db import models
from mothers.models import Mother

class Child(models.Model):
    mother = models.ForeignKey(Mother, on_delete=models.CASCADE, related_name='children')
    full_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=(('M', 'Male'), ('F', 'Female')))
    birth_weight = models.DecimalField(max_digits=5, decimal_places=2)
    place_of_birth = models.CharField(max_length=255)

    def __str__(self):
        return self.full_name

class GrowthRecord(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE, related_name='growth_records')
    date_measured = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    head_circumference = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.child.full_name} - {self.date_measured}"
