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

    categories = ["work", "sleep", "study", "hobby", "health"]
    quota = {}

    def perform_create(self, serializer: DailyQuotaSerializer):



        work = serializer.validated_data.get("work", None)
        sleep = serializer.validated_data.get("sleep", None)
        study = serializer.validated_data.get("study", None)
        hobby = serializer.validated_data.get("hobby", None)
        health = serializer.validated_data.get("health", None)

        quota = {
            "work": work,
            "sleep": sleep,
            "study": study,
            "hobby": hobby,
            "health": health,
        }

        serializer.save(**quota, user=self.request.user)



class DailyQuotaDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
