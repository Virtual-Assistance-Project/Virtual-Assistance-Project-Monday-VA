from django.urls import path
from . import views

urlpatterns = [
    path("infos/finance/", views.FinanceView.as_view()),
    path("infos/finance/profile/", views.FinanceDetails.as_view()),
]
