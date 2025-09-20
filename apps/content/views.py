from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import ShortCard
from .serializers import ShortCardSerializer

class ShortCardViewSet(viewsets.ModelViewSet):
    """
    List/Read for public; Create/Update kept open now for testing (AllowAny).
    Later make write-protected via IsAdminUser.
    """
    queryset = ShortCard.objects.all()
    serializer_class = ShortCardSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["active", "section", "locale", "media_type", "badge"]

    def get_queryset(self):
        qs = super().get_queryset()
        # Default: only active cards unless ?active= (explicitly provided)
        if "active" not in self.request.query_params:
            qs = qs.filter(active=True)
        # Order primary by order then id (Meta.ordering already does, still explicit slice support)
        return qs.order_by("order", "id")

    @action(detail=True, methods=["post"], url_path="track-view")
    def track_view(self, request, pk=None):
        obj = self.get_object()
        obj.view_count = (obj.view_count or 0) + 1
        obj.save(update_fields=["view_count"])
        return Response({"id": obj.id, "view_count": obj.view_count})
