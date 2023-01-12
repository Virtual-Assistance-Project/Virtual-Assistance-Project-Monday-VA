from .models import Schedule
from .serializers import ScheduleSerializer
from users.permissions import IsAccountOwner
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class ScheduleView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


class ScheduleDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer
