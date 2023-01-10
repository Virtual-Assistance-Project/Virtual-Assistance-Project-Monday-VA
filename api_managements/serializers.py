from rest_framework import serializers

from .models import APIManagement


class APIManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIManagement
        fields = "__all__"
