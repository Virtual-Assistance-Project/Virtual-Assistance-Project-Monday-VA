from rest_framework.views import Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Schedule
from .serializers import ScheduleSerializer
from users.permissions import IsAccountOwner
from utils.commons import CommonAppView, CommonAppDetailView


class ScheduleView(CommonAppView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetailView(CommonAppDetailView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get(self, request: Request) -> Response:
        schedules = Schedule.objects.filter(user=request.user)
        serializer = ScheduleSerializer(schedules, many=True)

        return Response(serializer.data, status.HTTP_200_OK)
