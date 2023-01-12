from rest_framework import serializers
from .models import HealthInfo


class HealthSerializer(serializers.ModelSerializer):
    type_bmi = serializers.SerializerMethodField()

    def get_type_bmi(self, obj):

        bmi = obj.bmi

        if 16 < bmi < 18.5:
            return "Underweight"
        elif 18.6 < bmi < 25:
            return "Normal"
        elif bmi > 25.1:
            return "Overweight"

    class Meta:
        model = HealthInfo
        fields = ["id", "height", "weight", "bmi", "type_bmi", "ideal_weight"]
        read_only_fields = ["bmi"]
