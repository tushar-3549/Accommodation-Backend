from django.db import models

class ShortCard(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=240, blank=True)
    thumbnail_url = models.URLField()
    target_url = models.URLField()
    view_count = models.PositiveIntegerField(default=0)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
