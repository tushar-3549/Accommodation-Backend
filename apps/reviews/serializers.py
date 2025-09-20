from rest_framework import serializers
from .models import Review

class UserLiteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Review
        # property ফিল্ডটা read-only রাখলাম; view থেকে slug দিয়ে সেট হবে
        fields = ["id", "user", "rating", "comment", "created_at", "property"]
        read_only_fields = ["user", "created_at", "property"]

    def get_user(self, obj):
        return {"id": obj.user_id, "username": getattr(obj.user, "username", "")}

    def validate_rating(self, value):
        if not (1 <= value <= 5):
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    def create(self, validated_data):
        # view -> perform_create এ property ও user সেট করে দেবে
        return super().create(validated_data)
