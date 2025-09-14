from rest_framework import serializers
from .models import Promotion, Campaign, Banner, FeaturedCollection, CollectionItem
from apps.property.serializers import PropertyCardSerializer
from apps.geo.serializers import CitySerializer

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ["id","name","description","badge_text","start_at","end_at"]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ["id","title","image_url","target_url","placement","order","active"]

class CollectionItemSerializer(serializers.ModelSerializer):
    property = PropertyCardSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    promotion = PromotionSerializer(read_only=True)
    class Meta:
        model = CollectionItem
        fields = ["item_type","order","property","city","promotion"]

class FeaturedCollectionSerializer(serializers.ModelSerializer):
    items = CollectionItemSerializer(many=True, read_only=True)
    class Meta:
        model = FeaturedCollection
        fields = ["id","title","subtitle","slug","order","active","items"]
