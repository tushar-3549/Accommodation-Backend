from rest_framework import serializers
from .models import ShortCard

class ShortCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortCard
        fields = ["id","title","subtitle","thumbnail_url","target_url","view_count","order"]
