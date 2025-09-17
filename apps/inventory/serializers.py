from rest_framework import serializers
from .models import NightlyPrice, NightlyInventory
from .services import compute_final_price

class NightlyPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NightlyPrice
        fields = ["id","property","room_type","rate_plan","stay_date",
                  "currency","base_price","final_price","discount_percent"]

    def validate(self, attrs):
        base = attrs.get("base_price")
        disc = attrs.get("discount_percent", 0)
        final = attrs.get("final_price")
        if base is not None and final is None:
            attrs["final_price"] = compute_final_price(base, disc)
        return attrs

class NightlyInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NightlyInventory
        fields = ["id","property","room_type","stay_date","allotment"]
