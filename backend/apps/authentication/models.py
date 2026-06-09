from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    class Role(models.TextChoices):
        MOTHER = 'MOTHER', 'Mother'
        NURSE = 'NURSE', 'Nurse'
        DOCTOR = 'DOCTOR', 'Doctor'
        CHW = 'CHW', 'Community Health Worker'
        ADMIN = 'ADMIN', 'Administrator'
        SUPER_ADMIN = 'SUPER_ADMIN', 'Super Administrator'
    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MOTHER)
    phone_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    must_change_password = models.BooleanField(default=True)
