from django.urls import path
from .views import QuoteView, BookingCreateView, BookingDetailView, MyBookingsView

urlpatterns = [
    path("bookings/quote", QuoteView.as_view()),
    path("bookings", BookingCreateView.as_view()),
    path("bookings/<str:code>", BookingDetailView.as_view()),
    path("me/bookings", MyBookingsView.as_view()),
]
