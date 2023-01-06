from django.urls import path
from .views import DailyQuotaView, DailyQuotaDetailView

urlpatterns = [
    path("daily/", DailyQuotaView.as_view()),
    path("daily/<uuid:pk>/", DailyQuotaDetailView.as_view()),
]
