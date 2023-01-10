from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import DailyQuota
from .serializers import DailyQuotaSerializer
from users.permissions import IsAccountOwner


class DailyQuotaView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = DailyQuotaSerializer

    def perform_create(self, serializer: DailyQuotaSerializer):

        quota = {
            "work": self.kwargs["work"] / 24,
            "sleep": self.kwargs["sleep"] / 24, 
            "study": self.kwargs["study"] / 24, 
            "hobby": self.kwargs["hobby"] / 24, 
            "health": self.kwargs["health"] / 24, 
        }
        
        serializer.save(quota)


class DailyQuotaDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    queryset = DailyQuota.objects.all()
    serializer_class = DailyQuotaSerializer
