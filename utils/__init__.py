from rest_framework.views import Response
from rest_framework.serializers import ModelSerializer


def custom_print(content):
    print("=" * 50)
    print(content)
    print("=" * 50)
