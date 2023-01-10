from django.urls import path
from . import views

urlpatterns = [
    path("infos/health/", views.HealthView.as_view()),
    path("infos/health/profile/", views.HealthDetailView.as_view()),
]
