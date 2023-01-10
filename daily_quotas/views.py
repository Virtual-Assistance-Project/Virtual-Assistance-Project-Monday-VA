from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from users.permissions import IsAccountOwner
from utils.commons import CommonInfoView, CommonInfoDetailView
import ipdb


class DailyQuotaView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = DailyQuotaSerializer
    queryset = DailyQuota.objects.all()

    def perform_create(self, serializer: DailyQuotaSerializer):

        work = serializer.validated_data.get("work", 0)
        sleep = serializer.validated_data.get("sleep", 0)
        study = serializer.validated_data.get("study", 0)
        hobby = serializer.validated_data.get("hobby", 0)
        health = serializer.validated_data.get("health", 0)

        quota = {
            "work": work / 24,
            "sleep": sleep / 24,
            "study": study / 24,
            "hobby": hobby / 24,
            "health": health / 24,
        }

        serializer.save(**quota, user=self.request.user)


class DailyQuotaDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
