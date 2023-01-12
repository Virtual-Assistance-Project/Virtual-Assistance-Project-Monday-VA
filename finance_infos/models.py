from django.db import models
from uuid import uuid4

from users.models import User


class Finance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    occupation = models.CharField(max_length=128)
    salary = models.IntegerField()
    salary_claim = models.IntegerField()
    is_retired = models.BooleanField(default=False)
