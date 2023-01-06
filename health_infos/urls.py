from django.urls import path
from . import views

urlpatterns = [
    path("health/", views.HealthView.as_view()),
    path("health/<uuid:pk>/", views.HealthDetailView.as_view()),
]
