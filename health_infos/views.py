from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from users.permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status

from .models import Heath_Info
from .serializers import HealthSerializer
from utils.commons import CommonInfoView, CommonInfoDetailView


class HealthView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_create(self, serializer: HealthSerializer):
        height = serializer.validated_data["height"]
        weight = serializer.validated_data["weight"]
        bmi = weight / (height**2)

        return serializer.save(bmi=bmi, user=self.request.user)


class HealthDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_update(self, serializer: HealthSerializer):
        instance: Heath_Info = self.get_object()
        height = serializer.validated_data.get("height", None) or instance.height
        weight = serializer.validated_data.get("weight", None) or instance.weight

        bmi = weight / (height**2)
        return serializer.save(bmi=bmi)
