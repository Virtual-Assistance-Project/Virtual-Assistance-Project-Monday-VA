from django.urls import path
from .views import DailyQuotaView, DailyQuotaDetailView

urlpatterns = [
    path("quotas/", DailyQuotaView.as_view()),
    path("quotas/profile/", DailyQuotaDetailView.as_view()),
]
