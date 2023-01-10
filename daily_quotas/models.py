from django.db import models
from uuid import uuid4

from users.models import User


class DailyQuota(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    work = models.DecimalField(max_digits=3, decimal_places=2)
    sleep = models.DecimalField(max_digits=3, decimal_places=2)
    study = models.DecimalField(max_digits=3, decimal_places=2)
    hobby = models.DecimalField(max_digits=3, decimal_places=2)
    health = models.DecimalField(max_digits=3, decimal_places=2)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="daily_quotas",
    )
