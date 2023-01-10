from rest_framework import serializers
from .models import DailyQuota


class DailyQuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyQuota
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True}
        }
