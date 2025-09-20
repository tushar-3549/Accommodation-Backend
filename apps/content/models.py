from django.db import models
from django.utils import timezone

class ShortCard(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = "IMAGE", "Image"
        VIDEO = "VIDEO", "Video"

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=240, blank=True)

    # media
    media_type = models.CharField(max_length=10, choices=MediaType.choices, default=MediaType.IMAGE)
    thumbnail_url = models.URLField()  # cover image (also used as poster for video)
    video_url = models.URLField(blank=True)  # optional, when media_type=VIDEO
    aspect_ratio = models.CharField(max_length=10, blank=True)  # e.g. "16:9", "1:1", "9:16"

    # navigation
    target_url = models.URLField()

    # taxonomy / display
    locale = models.CharField(max_length=8, default="en")  # e.g. "en", "ko", "ja"
    section = models.CharField(max_length=50, default="home")  # e.g. "home", "global"
    badge = models.CharField(max_length=30, blank=True)  # e.g. "NEW", "HOT"
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)

    # tracking
    view_count = models.PositiveIntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        indexes = [
            models.Index(fields=["active", "section", "locale", "order"]),
        ]
        ordering = ["order", "id"]

    def __str__(self):
        return f"[{self.section}/{self.locale}] {self.title}"
