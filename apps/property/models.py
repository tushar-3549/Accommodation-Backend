from django.db import models
from slugify import slugify
from apps.geo.models import City

class Amenity(models.Model):
    name = models.CharField(max_length=120, unique=True)
    icon = models.CharField(max_length=120, blank=True)  # frontend icon key
    def __str__(self): return self.name

class Property(models.Model):
    class Category(models.TextChoices):
        HOTEL = "HOTEL", "Hotel"
        RESORT = "RESORT", "Resort"
        VILLA = "VILLA", "Villa"
        APARTHOTEL = "APARTHOTEL", "Aparthotel"

    city = models.ForeignKey(City, on_delete=models.PROTECT, related_name="properties")
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.HOTEL)
    address = models.CharField(max_length=240, blank=True)
    star_rating = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    amenities = models.ManyToManyField(Amenity, related_name="properties", blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        unique_together = ("city", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city.slug}")
        super().save(*args, **kwargs)

    def __str__(self): return self.name

class Media(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="media")
    url = models.URLField()
    is_primary = models.BooleanField(default=False)
    alt = models.CharField(max_length=150, blank=True)

class RoomType(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="room_types")
    name = models.CharField(max_length=160)
    capacity_adults = models.PositiveIntegerField(default=2)
    capacity_children = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("property", "name")

    def __str__(self): return f"{self.property.name} - {self.name}"

class RatePlan(models.Model):
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, related_name="rate_plans")
    name = models.CharField(max_length=160)  # e.g. "Standard", "Breakfast Included"
    refundable = models.BooleanField(default=True)
    cancellation_policy = models.TextField(blank=True)

    class Meta:
        unique_together = ("room_type", "name")

    def __str__(self): return f"{self.room_type.name} - {self.name}"
