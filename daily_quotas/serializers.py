from rest_framework import serializers
from .models import DailyQuota


class DailyQuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyQuota
        fields = ["id", "type", "work", "sleep", "study", "hobby", "health"]
        extra_kwargs = {"user": {"read_only": True}, "type": {"write_only": True}}
