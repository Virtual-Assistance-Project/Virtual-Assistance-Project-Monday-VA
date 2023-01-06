from django.urls import path
from . import views

urlpatterns = [
    path("finance/", views.FinanceView.as_view()),
    path("finance/<uuid:finance_id>", views.FinanceDetails.as_view()),
]
