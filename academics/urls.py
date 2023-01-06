from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from . import views
from .views import AcademicView

urlpatterns = [
    path("academics/", views.AcademicView.as_view()),
    path("academics/<uuid:pk>", views.AcademicDetailView.as_view()),
]
