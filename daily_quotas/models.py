from django.db import models
from uuid import uuid4

from users.models import User


class QuotaType(models.Choices):
    DAILY = "daily"
    DEFAULT = "total"


class DailyQuota(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    type = models.CharField(
        max_length=32, choices=QuotaType.choices, default=QuotaType.DEFAULT
    )
    work = models.FloatField(default=0)
    sleep = models.FloatField(default=0)
    study = models.FloatField(default=0)
    hobby = models.FloatField(default=0)
    health = models.FloatField(default=0)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="daily_quota",
        null=True,
    )