from rest_framework.serializers import ModelSerializer, SerializerMethodField

from finance_infos.models import Finance
from users.models import User


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
