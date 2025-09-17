from rest_framework import serializers
from .models import Review

class UserLiteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    username = serializers.CharField()

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = ["id","user","rating","comment","created_at","property"]
        read_only_fields = ["user","created_at"]

    def get_user(self, obj):
        return {"id": obj.user_id, "username": obj.user.username}

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)
