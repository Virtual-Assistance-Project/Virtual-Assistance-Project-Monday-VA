from rest_framework.generics import ListCreateAPIView

from .models import Heath_Info
from .serializers import HealthSerializer
import ipdb


class HealthView(ListCreateAPIView):
    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_create(self, serializer):
        height = serializer.validated_data["height"]
        weight = serializer.validated_data["weight"]

        return serializer.save(bmi=round(weight / (height * height)))
