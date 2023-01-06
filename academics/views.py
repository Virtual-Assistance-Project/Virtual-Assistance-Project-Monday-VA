from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from users.models import User

from .models import Academic
from .serializers import AcademicSerializer


class AcademicView(CreateAPIView):
    permission_classes = [JWTAuthentication]

    def perform_create(self, serializer: AcademicSerializer):
        user = get_object_or_404(User, id=self.request.user)
        return serializer.save(user_id=user)


class AcademicDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [JWTAuthentication]
    serializer_class = AcademicSerializer()       
    queryset = Academic.objects.all()
