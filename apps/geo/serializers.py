from rest_framework import serializers
from .models import Country, City, Landmark

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ["id", "name", "code", "slug"]

class CitySerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = City
        fields = ["id", "name", "slug", "country", "is_featured"]

class LandmarkSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True)
    class Meta:
        model = Landmark
        fields = ["id", "name", "slug", "city"]
