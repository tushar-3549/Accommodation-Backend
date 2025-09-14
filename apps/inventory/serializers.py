from rest_framework import serializers
from .models import NightlyPrice, NightlyInventory

class NightlyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightlyPrice
        fields = ["id","property","room_type","rate_plan","stay_date",
                  "currency","base_price","final_price","discount_percent"]

class NightlyInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NightlyInventory
        fields = ["id","property","room_type","stay_date","allotment"]
