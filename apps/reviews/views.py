from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer

class PropertyReviewListCreate(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Review.objects.select_related("user","property").filter(property__slug=slug)

    def perform_create(self, serializer):
        self.permission_classes = [permissions.IsAuthenticated]
        serializer.save()
