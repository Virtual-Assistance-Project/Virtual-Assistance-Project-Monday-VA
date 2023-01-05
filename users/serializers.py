from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "birthdate",
            "first_name",
            "last_name",
        ]
        extra_kwargs = {
            "username": {
                "validators": [
                    UniqueValidator(
                        User.objects.all(), "A user with that username already exists."
                    ),
                ],
            },
            "email": {
                "validators": [
                    UniqueValidator(User.objects.all(), "This field must be unique."),
                ],
            },
            "password": {"write_only": True},
            "is_staff": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if validated_data["username"] == "admin":
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        instance.save()
        return instance
