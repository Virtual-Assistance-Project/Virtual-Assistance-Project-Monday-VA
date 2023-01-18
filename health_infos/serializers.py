from rest_framework import serializers
from .models import HealthInfo

from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Criação Informações Saúde",
            summary="Informações de saúde",
            description="Rota para criação de informações sobre saúde",
            value={"height": 1.84, "weight": 91.8, "ideal_weight": 85},
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Criação Informações Saúde",
            summary="Informações de saúde",
            description="Rota para criação de informações sobre saúde",
            value={
                "id": "5e231291-ec55-4151-984d-57b57c1981f0",
                "height": "1.84",
                "weight": "91.80",
                "bmi": "27.11",
                "type_bmi": "Overweight",
                "ideal_weight": 85,
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
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
