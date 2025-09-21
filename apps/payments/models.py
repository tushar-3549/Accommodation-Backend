from django.db import models
from django.conf import settings

class Payment(models.Model):
    class Status(models.TextChoices):
        REQUIRES_CONFIRMATION = "requires_confirmation"
        SUCCEEDED = "succeeded"
        FAILED = "failed"
        CANCELED = "canceled"

    # optional: কোন user/booking এর সাথে সম্পর্ক (চাইলেই null রাখো)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="payments"
    )
    booking_code = models.CharField(max_length=32, blank=True)  # e.g. BK-...
    provider = models.CharField(max_length=32, default="mock")
    currency = models.CharField(max_length=3, default="KRW")
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    client_secret = models.CharField(max_length=64, unique=True)  # e.g. pi_xxx
    status = models.CharField(max_length=24, choices=Status.choices, default=Status.REQUIRES_CONFIRMATION)

    # audit
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # useful flags
    metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"{self.client_secret} ({self.status})"
