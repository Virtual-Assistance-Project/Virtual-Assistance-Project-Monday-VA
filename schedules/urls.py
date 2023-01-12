from django.urls import path
from . import views

urlpatterns = [
    path("schedules/", views.ScheduleView.as_view()),
    path("schedules/profile/", views.ScheduleDetailView.as_view()),
]
