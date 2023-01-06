from django.db import models
from uuid import uuid4


class DailyQuota(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    work = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    sleep = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    study = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    hobby = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    health = models.DecimalField(max_digits=3, decimal_places=2, null=True)
