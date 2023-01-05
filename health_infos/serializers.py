from rest_framework import serializers
from .models import Heath_Info


class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heath_Info
        fields = ["id", "height", "weight", "bmi", "ideal_weight"]
        read_only_fields = ["bmi"]
