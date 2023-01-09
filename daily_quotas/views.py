from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from users.permissions import IsAccountOwnerOrSuperuser


class DailyQuotaView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    serializer_class = DailyQuotaSerializer

    def perform_create(self, serializer: DailyQuotaSerializer):

        quota = {
            "work_percentage": self.kwargs["work"] / 24,
            "sleep_percentage": self.kwargs["sleep"] / 24, 
            "sludy_percentage": self.kwargs["sludy"] / 24, 
            "hobby_percentage": self.kwargs["hobby"] / 24, 
            "health_percentage": self.kwargs["health"] / 24, 
        }
        
        serializer.save(quota)


class DailyQuotaDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
