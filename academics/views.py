from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User

from .models import Academic
from .serializers import AcademicSerializer


class AcademicView(CreateAPIView):
    permission_classes = [JWTAuthentication]

    def create(self, request: Request) -> Response:
        serializer = AcademicSerializer()
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer, request)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer: AcademicSerializer, request: Request):
        user = get_object_or_404(User, id=request.user.id)
        return serializer.save(user_id=user)


class AcademicDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [JWTAuthentication]
