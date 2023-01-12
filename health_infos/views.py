from .models import HealthInfo
from .serializers import HealthSerializer
from utils.commons import CommonAppView, CommonAppDetailView


class HealthView(CommonAppView):
    serializer_class = HealthSerializer
    queryset = HealthInfo.objects.all()

    def perform_create(self, serializer: HealthSerializer):
        height = serializer.validated_data["height"]
        weight = serializer.validated_data["weight"]
        bmi = weight / (height**2)

        return serializer.save(bmi=bmi, user=self.request.user)


class HealthDetailView(CommonAppDetailView):
    serializer_class = HealthSerializer
    queryset = HealthInfo.objects.all()

    def perform_update(self, serializer: HealthSerializer):
        instance: HealthInfo = self.get_object()
        height = serializer.validated_data.get("height", None) or instance.height
        weight = serializer.validated_data.get("weight", None) or instance.weight

        bmi = weight / (height**2)
        return serializer.save(bmi=bmi)
