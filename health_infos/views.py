from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Heath_Info
from .serializers import HealthSerializer


class HealthView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_create(self, serializer: HealthSerializer):
        height = serializer.validated_data["height"]
        weight = serializer.validated_data["weight"]
        bmi = weight / (height**2)

        return serializer.save(bmi=bmi)


class HealthDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_update(self, serializer: HealthSerializer):
        height = self.get_object().height
        height_a = serializer.validated_data.get("height", None)
        weight = serializer.validated_data.get("weight", None)

        if height_a and weight is None:

            if height_a:
                bmi = weight / (height_a**2)
                updated_instance = serializer.save(bmi=bmi)

            bmi = weight / (height**2)

            updated_instance = serializer.save(bmi=bmi)

            return updated_instance

        return serializer.save()
