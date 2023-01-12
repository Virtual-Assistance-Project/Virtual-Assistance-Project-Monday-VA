from django.db import models
from uuid import uuid4


class ScheduleType(models.Choices):
    WORK = "work"
    SLEEP = "sleep"
    STUDY = "study"
    HOBBY = "hobby"
    HEALTH = "health"
    DEFAULT = "commitment"


class Schedule(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, unique=True)
    title = models.CharField(max_length=128)
    type = models.CharField(
        max_length=16, choices=ScheduleType.choices, default=ScheduleType.DEFAULT
    )
    begans_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    description = models.TextField(null=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="user",
        null=True,
    )
