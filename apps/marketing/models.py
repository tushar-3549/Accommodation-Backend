from django.db import models
from django.utils import timezone
from apps.property.models import Property
from apps.geo.models import City

class Promotion(models.Model):
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    badge_text = models.CharField(max_length=40, blank=True)  # e.g., "37% OFF"
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    properties = models.ManyToManyField(Property, related_name="promotions", blank=True)

    @property
    def active(self) -> bool:
        now = timezone.now()
        return self.start_at <= now <= self.end_at
    
    class Meta:
        ordering = ["-start_at", "id"]
        indexes = [models.Index(fields=["start_at", "end_at"])]



class Campaign(models.Model):
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True)
    description = models.TextField(blank=True)
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)

class Banner(models.Model):
    class Placement(models.TextChoices):
        GLOBAL_HOME_TOP = "global_home_top", "Global Home Top"
        GLOBAL_HOME_MID = "global_home_mid", "Global Home Mid"

    title = models.CharField(max_length=160, blank=True)
    image_url = models.URLField()
    target_url = models.URLField(blank=True)
    placement = models.CharField(max_length=40, choices=Placement.choices)
    campaign = models.ForeignKey(Campaign, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["placement", "order", "id"]
        indexes = [models.Index(fields=["placement", "active"])]

class FeaturedCollection(models.Model):
    title = models.CharField(max_length=160)
    subtitle = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ["order", "id"]


class CollectionItem(models.Model):
    class ItemType(models.TextChoices):
        PROPERTY = "PROPERTY", "Property"
        CITY = "CITY", "City"
        PROMOTION = "PROMOTION", "Promotion"

    collection = models.ForeignKey(FeaturedCollection, on_delete=models.CASCADE, related_name="items")
    item_type = models.CharField(max_length=20, choices=ItemType.choices)
    property = models.ForeignKey(Property, null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, null=True, blank=True, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
