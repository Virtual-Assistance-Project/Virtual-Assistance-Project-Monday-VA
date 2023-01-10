from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Academic
from .serializers import AcademicSerializer
from utils.commons import CommonInfoView, CommonInfoDetailView


class AcademicView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()


class AcademicDetailView(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()
