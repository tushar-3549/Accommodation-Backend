from rest_framework import mixins, viewsets
from .models import ShortCard
from .serializers import ShortCardSerializer

class ShortCardViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = ShortCardSerializer
    queryset = ShortCard.objects.filter(active=True).order_by("order","id")
