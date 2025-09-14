from django.db import models
from apps.property.models import Property, RoomType, RatePlan

class NightlyInventory(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="inventories")
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    stay_date = models.DateField()
    allotment = models.PositiveIntegerField(default=0)  # remaining rooms

    class Meta:
        unique_together = ("property", "room_type", "stay_date")

class NightlyPrice(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="prices")
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    rate_plan = models.ForeignKey(RatePlan, on_delete=models.CASCADE)
    stay_date = models.DateField()
    currency = models.CharField(max_length=3, default="KRW")
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percent = models.IntegerField(default=0)

    class Meta:
        unique_together = ("property", "room_type", "rate_plan", "stay_date", "currency")
        indexes = [
            models.Index(fields=["property", "stay_date"]),
            models.Index(fields=["currency"]),
        ]
