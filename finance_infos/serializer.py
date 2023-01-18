from rest_framework.serializers import ModelSerializer, SerializerMethodField

from finance_infos.models import Finance
from users.models import User

from drf_spectacular.utils import extend_schema_serializer
from drf_spectacular.utils import OpenApiExample


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            "Criação Informações Finanças",
            summary="Informações de finanças",
            description="Rota para criação de informações sobre finanças",
            value={
                "occupation": "Sofware Engineer",
                "salary": 4500,
                "salary_claim": 7000,
            },
            request_only=True,
            response_only=False,
        ),
        OpenApiExample(
            "Criação Informações Finanças",
            summary="Informações de finanças",
            description="Rota para criação de informações sobre finanças",
            value={
                "id": "e10f5549-b3f7-408a-a2ea-983d47b221ec",
                "occupation": "Sofware Engineer",
                "salary": 4500,
                "salary_claim": 7000,
                "is_retired": False,
                "user_id": "faa96109-3895-4be3-9201-f68291d503e0",
            },
            request_only=False,
            response_only=True,
        ),
    ]
)
class FinanceSerializer(ModelSerializer):

    user_id = SerializerMethodField()

    def get_user_id(self, obj: User):
        return obj.user.id

    class Meta:
        model = Finance
        fields = [
            "id",
            "occupation",
            "salary",
            "salary_claim",
            "is_retired",
            "user_id",
        ]
