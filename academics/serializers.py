from rest_framework import serializers

from .models import Academic, Level


class AcademicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Academic
        fields = ["id", "educational_level", "is_graduated", "main_graduation"]
        extra_kwargs = {
            "educational_level": {
                "choices": Level.choices, "default": Level.DEFAULT
            },
        }
