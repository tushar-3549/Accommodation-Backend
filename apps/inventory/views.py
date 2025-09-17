from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import NightlyPrice, NightlyInventory
from .serializers import NightlyPriceSerializer, NightlyInventorySerializer
from .filters import NightlyPriceFilter, NightlyInventoryFilter

class NightlyPriceViewSet(viewsets.ModelViewSet):
    queryset = NightlyPrice.objects.all().order_by("stay_date")
    serializer_class = NightlyPriceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NightlyPriceFilter
    permission_classes = [permissions.AllowAny]

class NightlyInventoryViewSet(viewsets.ModelViewSet):
    queryset = NightlyInventory.objects.all().order_by("stay_date")
    serializer_class = NightlyInventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NightlyInventoryFilter
    permission_classes = [permissions.AllowAny]
