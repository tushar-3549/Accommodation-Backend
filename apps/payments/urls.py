from django.urls import path
from .views import PaymentIntentView

urlpatterns = [
    path("payments/intents", PaymentIntentView.as_view()),
]
