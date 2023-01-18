from rest_framework import serializers
from .models import DailyQuota

from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Criação Daily Quotas",
            summary="Daily Quotas",
            description="Rota para criação de daily quotas",
            value={"type": "total", "work": 8, "sleep": 8, "study": 2, "hobby": 1},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Criação Daily Quotas",
            summary="Daily Quotas",
            description="Rota para criação de daily quotas",
            value={
                "id": "9ffd7863-4760-4f09-9cb3-cbb997ff877c",
                "work": 0.421,
                "sleep": 0.421,
                "study": 0.105,
                "hobby": 0.053,
                "health": 0.0,
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class DailyQuotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyQuota
        fields = ["id", "type", "work", "sleep", "study", "hobby", "health"]
        extra_kwargs = {"user": {"read_only": True}, "type": {"write_only": True}}
