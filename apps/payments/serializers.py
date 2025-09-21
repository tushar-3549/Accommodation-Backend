from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = [
            "id","client_secret","provider","amount","currency","status",
            "booking_code","metadata","created_at","updated_at"
        ]
        read_only_fields = ["id","status","created_at","updated_at","client_secret"]
