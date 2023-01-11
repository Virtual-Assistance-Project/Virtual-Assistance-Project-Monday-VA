from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.conversions import quota_to_percentage

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from users.permissions import IsAccountOwner
from utils.commons import CommonInfoView, CommonInfoDetailView


class DailyQuotaView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = DailyQuotaSerializer
    queryset = DailyQuota.objects.all()

    def perform_create(self, serializer: DailyQuotaSerializer):
        percentage = quota_to_percentage(serializer)
        serializer.save(**percentage, user=self.request.user)


class DailyQuotaDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer

    def perform_update(self, serializer: DailyQuotaSerializer):
        percentage = quota_to_percentage(serializer)
        serializer.save(**percentage)
