from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Country, City, Landmark
from .serializers import CountrySerializer, CitySerializer, LandmarkSerializer

class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Country.objects.all().order_by("name")
    serializer_class = CountrySerializer

class CityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = City.objects.select_related("country").all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["country", "is_featured"]

class LandmarkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Landmark.objects.select_related("city", "city__country").all()
    serializer_class = LandmarkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["city"]
