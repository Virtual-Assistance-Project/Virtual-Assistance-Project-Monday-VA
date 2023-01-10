from rest_framework.generics import RetrieveAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from api_managements.models import APIManagement
from api_managements.serializers import APIManagementSerializer

from users.permissions import IsAccountOwner


class APIManagementViews(RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    serializer_class = APIManagementSerializer

    def get_queryset(self):
        return APIManagement.objects.filter(user=self.request.user)
