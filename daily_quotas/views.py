from utils.conversions import quota_to_percentage

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from utils.commons import CommonAppView, CommonAppDetailView


class DailyQuotaView(CommonAppView):
    serializer_class = DailyQuotaSerializer
    queryset = DailyQuota.objects.all()

    def perform_create(self, serializer: DailyQuotaSerializer):
        percentage = quota_to_percentage(serializer)
        serializer.save(**percentage, user=self.request.user)


class DailyQuotaDetailView(CommonAppDetailView):
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer

    def perform_update(self, serializer: DailyQuotaSerializer):
        percentage = quota_to_percentage(serializer)
        serializer.save(**percentage)
