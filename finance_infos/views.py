from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


from finance_infos.models import Finance
from finance_infos.serializer import FinanceSerializer


class FinanceView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer

    def perform_create(self, serializer: FinanceSerializer):
        serializer.save(user=self.request.user)


class FinanceDetails(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
    lookup_url_kwarg = "finance_id"
