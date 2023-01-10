from django.urls import path

from . import views

urlpatterns = [
    path("infos/academics/", views.AcademicView.as_view()),
    path("infos/academics/profile/", views.AcademicDetailView.as_view()),
]
