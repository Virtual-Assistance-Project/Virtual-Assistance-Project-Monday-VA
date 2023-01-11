from rest_framework.serializers import ModelSerializer
from rest_framework.views import status
from django.core.exceptions import ValidationError


def quota_to_percentage(serializer: ModelSerializer) -> dict:
    quotas = {
        "work": serializer.validated_data.get("work", 0),
        "sleep": serializer.validated_data.get("sleep", 0),
        "study": serializer.validated_data.get("study", 0),
        "hobby": serializer.validated_data.get("hobby", 0),
        "health": serializer.validated_data.get("health", 0),
    }
    quota_type = serializer.validated_data.get("type", "total")

    base_quota = 0
    for value in quotas.values():
        base_quota += value

    if quota_type == "daily" and base_quota > 24:
        raise ValidationError(
            "When declaring type = 'daily' ensure that the sum of the quotas does not exceed 24 hours.",
            status.HTTP_400_BAD_REQUEST,
        )

    for key, value in quotas.items():
        quotas.update(
            {key: round(value / 24 if quota_type == "daily" else value / base_quota, 3)}
        )

    return quotas
