from django.db import models
from django.conf import settings
from apps.property.models import Property, RoomType, RatePlan

class Booking(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING"
        CONFIRMED = "CONFIRMED"
        CANCELLED = "CANCELLED"

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="bookings")
    code = models.CharField(max_length=20, unique=True)
    property = models.ForeignKey(Property, on_delete=models.PROTECT)
    room_type = models.ForeignKey(RoomType, on_delete=models.PROTECT)
    rate_plan = models.ForeignKey(RatePlan, on_delete=models.PROTECT)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveSmallIntegerField(default=2)
    children = models.PositiveSmallIntegerField(default=0)
    currency = models.CharField(max_length=3, default="KRW")
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.PENDING)
    payment_intent = models.CharField(max_length=64, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
