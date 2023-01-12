from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from uuid import uuid4


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthdate = models.DateField()

    # Managements
    auto_schedule = models.BooleanField(default=False)
    academic_infos = models.OneToOneField(
        "academics.Academic",
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
    )
    daily_quotas = models.OneToOneField(
        "daily_quotas.DailyQuota",
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
    )
    finance_infos = models.OneToOneField(
        "finance_infos.Finance",
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
    )
    health_infos = models.OneToOneField(
        "health_infos.HealthInfo",
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
    )

    # Redeclaration made for typing recognition when creating a new user.
    objects = UserManager()
