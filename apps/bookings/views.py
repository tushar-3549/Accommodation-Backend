import random, string
from datetime import datetime
from rest_framework import generics, permissions, views
from rest_framework.response import Response
from .models import Booking
from .serializers import BookingSerializer, BookingBriefSerializer
from .services import quote_total


def _code():
    return f"BK-{datetime.utcnow():%Y%m%d}-{''.join(random.choices(string.ascii_uppercase, k=4))}"


class QuoteView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        d = request.data
        q = quote_total(
            d["property"],
            d["room_type"],
            d["rate_plan"],
            datetime.fromisoformat(d["check_in"]).date(),
            datetime.fromisoformat(d["check_out"]).date(),
            d.get("currency", "KRW"),
        )
        q["currency"] = d.get("currency", "KRW")
        return Response(q, 200)


class BookingCreateView(generics.CreateAPIView):
    serializer_class = BookingSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        data = serializer.validated_data
        # auto total_price if not provided
        if not data.get("total_price"):
            q = quote_total(
                data["property"].id,
                data["room_type"].id,
                data["rate_plan"].id,
                data["check_in"],
                data["check_out"],
                data.get("currency", "KRW"),
            )
            data["total_price"] = q["total"]

        code = _code()
        # serializer.save(user=self.request.user, code=code, status="CONFIRMED")
        serializer.save(code=code, status="CONFIRMED")


class BookingDetailView(generics.RetrieveAPIView):
    serializer_class = BookingSerializer
    lookup_field = "code"
    queryset = Booking.objects.all()


class MyBookingsView(generics.ListAPIView):
    serializer_class = BookingBriefSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        # return Booking.objects.filter(user=self.request.user)
        return Booking.objects.all()
