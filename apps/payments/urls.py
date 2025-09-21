# from django.urls import path
# from .views import PaymentIntentView

# urlpatterns = [
#     path("payments/intents", PaymentIntentView.as_view()),
# ]



from django.urls import path
from .views import PaymentIntentView, PaymentConfirmView

urlpatterns = [
    path("payments/intents", PaymentIntentView.as_view()),
    path("payments/intents/<str:client_secret>/confirm", PaymentConfirmView.as_view()),
]
