from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        read_only_fields = ["code","status","user","created_at"]

class BookingBriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["code","status","property","check_in","check_out","currency","total_price","created_at"]
