from django.db import models
from uuid import uuid4

options = (
    ('WORK', 'Trabalho'),
    ('SLEEP', 'Dormindo'),
    ('STUDY', 'Estudo'),
    ('HOBBY', 'Hobby'),
    ('HEALTH', 'Saúde'),
    ('COMMITMENT', 'Compromisso')
)

class Schedule(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid4, 
        unique=True
    )
    title = models.CharField(max_length=128)
    type = models.ChoiceField(
        max_length=16, 
        choices=options,
        default="COMMITMENT"
    )
    begans_at = models.DateTimeField()
    ends_at = models.DateTimeField(defaut=begans_at)
    routine_weekdays = models.CharField(max_length=23)
    description = models.TextField(max_length=500)
    management_id = models.ForeignKey()