from rest_framework import viewsets, mixins
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from .models import Promotion, Banner, FeaturedCollection
from .serializers import PromotionSerializer, BannerSerializer, FeaturedCollectionSerializer

class PromotionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PromotionSerializer
    def get_queryset(self):
        now = timezone.now()
        return Promotion.objects.filter(start_at__lte=now, end_at__gte=now)

class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = BannerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["placement"]
    queryset = Banner.objects.filter(active=True).order_by("placement","order")

class FeaturedCollectionViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = FeaturedCollectionSerializer
    queryset = FeaturedCollection.objects.filter(active=True).order_by("order").prefetch_related("items__property__media","items__city","items__promotion")
