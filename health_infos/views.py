from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from users.permissions import IsAccountOwner
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from rest_framework.views import Request, Response, status

from .models import Heath_Info
from .serializers import HealthSerializer


class HealthView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def perform_create(self, serializer: HealthSerializer):
        height = serializer.validated_data["height"]
        weight = serializer.validated_data["weight"]
        bmi = weight / (height**2)

        return serializer.save(bmi=bmi, user=self.request.user)

    def create(self, request: Request, *args, **kwargs) -> Response:
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {
                    "detail": "This user already has this type of information registered. Try to update it."
                },
                status.HTTP_409_CONFLICT,
            )


class HealthDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = HealthSerializer
    queryset = Heath_Info.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user_id=self.request.user)

    def get_object(self):
        return get_object_or_404(self.get_queryset(), user=self.request.user)

    def perform_update(self, serializer: HealthSerializer):
        instance: Heath_Info = self.get_object()
        height = serializer.validated_data.get("height", None) or instance.height
        weight = serializer.validated_data.get("weight", None) or instance.weight

        bmi = weight / (height**2)
        return serializer.save(bmi=bmi)
