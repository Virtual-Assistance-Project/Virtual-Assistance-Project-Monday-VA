from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from users.permissions import IsAccountOwner

from utils.commons import CommonInfoView, CommonInfoDetailView



class DailyQuotaView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = DailyQuotaSerializer
    queryset = DailyQuota.objects.all()

    categories = ["work", "sleep", "study", "hobby", "health"]
    quota = {}

    def perform_create(self, serializer: DailyQuotaSerializer):

        for elem in self.categories:
            if serializer.validated_data[elem] is True:
                self.quota[elem] = serializer.validated_data[elem] / 24
            else: 
                self.quota[elem] = None

        
        serializer.save(**self.quota)


class DailyQuotaDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
