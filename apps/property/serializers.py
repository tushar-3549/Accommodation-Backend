from rest_framework import serializers
from .models import Amenity, Property, Media, RoomType, RatePlan
from apps.geo.serializers import CitySerializer

class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        fields = ["id", "name", "icon"]

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ["url", "is_primary", "alt"]

class RatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatePlan
        fields = ["id", "name", "refundable", "cancellation_policy"]

class RoomTypeSerializer(serializers.ModelSerializer):
    rate_plans = RatePlanSerializer(many=True, read_only=True)
    class Meta:
        model = RoomType
        fields = ["id", "name", "capacity_adults", "capacity_children", "rate_plans"]

class PropertyCardSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    cover_image = serializers.SerializerMethodField()
    min_price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    currency = serializers.CharField(read_only=True)
    discount_percent = serializers.IntegerField(read_only=True)

    class Meta:
        model = Property
        fields = ["id", "name", "slug", "category", "star_rating", "city",
                  "cover_image", "min_price", "currency", "discount_percent"]

    def get_cover_image(self, obj):
        m = obj.media.filter(is_primary=True).first() or obj.media.first()
        return m.url if m else None

class PropertyDetailSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    media = MediaSerializer(many=True, read_only=True)
    room_types = RoomTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = ["id", "name", "slug", "category", "address", "star_rating",
                  "latitude", "longitude", "city", "amenities", "media", "room_types"]
