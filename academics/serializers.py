from rest_framework import serializers

from .models import Academic


class AcademicSerializer(serializers.ModelSerializer):

    class Meta:

        model = Academic
        fields = ["id", "educational_level", "is_graduated", "main_graduation"]

    def create(self, validated_data):
        return Academic.objects.create(**validated_data)

    def update(self, instance: Academic, validated_data: dict) -> Academic:
        for key, value in validated_data.items():
            setattr(instance, key, value)

            instance.save()

        return instance
