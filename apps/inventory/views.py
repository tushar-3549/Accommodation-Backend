from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import NightlyPrice, NightlyInventory
from .serializers import NightlyPriceSerializer, NightlyInventorySerializer

class NightlyPriceViewSet(viewsets.ModelViewSet):
    queryset = NightlyPrice.objects.all().order_by("stay_date")
    serializer_class = NightlyPriceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["property","room_type","rate_plan","stay_date","currency"]
    permission_classes = [permissions.IsAdminUser]

class NightlyInventoryViewSet(viewsets.ModelViewSet):
    queryset = NightlyInventory.objects.all().order_by("stay_date")
    serializer_class = NightlyInventorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["property","room_type","stay_date"]
    permission_classes = [permissions.IsAdminUser]
