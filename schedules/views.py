from .models import Schedule
from .serializers import ScheduleSerializer
from users.permissions import IsAccountOwnerOrSuperuser 
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class ScheduleListCreateView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

class ScheduleRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrSuperuser]
    
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer