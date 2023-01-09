from django.db import models
from uuid import uuid4

class APIManagement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    auto_schedule = models.BooleanField(default=False)
    active_time = models.DecimalField(max_digits=3, decimal_places=2, null=True)
    

