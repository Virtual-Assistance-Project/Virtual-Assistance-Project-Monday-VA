from .models import Academic
from .serializers import AcademicSerializer
from utils.commons import CommonAppView, CommonAppDetailView


class AcademicView(CommonAppView):
    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()


class AcademicDetailView(CommonAppDetailView):
    serializer_class = AcademicSerializer
    queryset = Academic.objects.all()
