from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

from utils.commons import CommonAppView, CommonAppDetailView
from finance_infos.models import Finance
from finance_infos.serializer import FinanceSerializer


class FinanceView(CommonAppView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer


class FinanceDetails(CommonAppDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Finance.objects.all()
    serializer_class = FinanceSerializer
