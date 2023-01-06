from rest_framework import serializers

from .models import Academic


class AcademicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Academic
        fields = ["id", "educational_level", "is_graduated", "main_graduation"]
