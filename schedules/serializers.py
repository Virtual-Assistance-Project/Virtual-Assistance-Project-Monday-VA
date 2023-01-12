from rest_framework import serializers
from .models import Schedule


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            "id",
            "title",
            "type",
            "begans_at",
            "ends_at",
            "description",
        ]
