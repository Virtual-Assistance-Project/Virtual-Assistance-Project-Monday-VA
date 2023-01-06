from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Heath_Info(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    height = models.DecimalField(max_digits=3, decimal_places=2)
    weight = models.DecimalField(max_digits=8, decimal_places=2)
    bmi = models.DecimalField(max_digits=4, decimal_places=2)
    ideal_weight = models.IntegerField()
