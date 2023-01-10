from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.commons import CommonInfoView, CommonInfoDetailView
from finance_infos.models import Finance
from finance_infos.serializer import FinanceSerializer


class FinanceView(CommonInfoView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


class FinanceDetails(CommonInfoDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
