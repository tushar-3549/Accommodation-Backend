from django.db import models
from slugify import slugify

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=2, unique=True)  # ISO-2
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self): return self.name

class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="cities")
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    is_featured = models.BooleanField(default=False)

    class Meta:
        unique_together = ("country", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.country.code}")
        super().save(*args, **kwargs)

    def __str__(self): return f"{self.name}, {self.country.code}"

class Landmark(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="landmarks")
    name = models.CharField(max_length=160)
    slug = models.SlugField(max_length=180, unique=True, blank=True)

    class Meta:
        unique_together = ("city", "name")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.city.slug}")
        super().save(*args, **kwargs)

    def __str__(self): return self.name
