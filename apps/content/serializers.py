from rest_framework import serializers
from .models import ShortCard

class ShortCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortCard
        fields = [
            "id", "title", "subtitle",
            "media_type", "thumbnail_url", "video_url", "aspect_ratio",
            "target_url",
            "locale", "section", "badge",
            "order", "active",
            "view_count", "created_at",
        ]
        read_only_fields = ["view_count", "created_at"]
