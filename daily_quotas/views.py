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

    def perform_create(self, serializer: DailyQuotaSerializer):
        quota = {
            "work": serializer.validated_data["work"] / 24,
            "sleep": serializer.validated_data["sleep"] / 24, 
            "study": serializer.validated_data["study"] / 24, 
            "hobby": serializer.validated_data["hobby"] / 24, 
            "health": serializer.validated_data["health"] / 24, 
        }
        
        serializer.save(**quota)


class DailyQuotaDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
