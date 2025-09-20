from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from apps.property.models import Property


from django.contrib.auth import get_user_model
User = get_user_model()

class PropertyReviewListCreate(generics.ListCreateAPIView):
    """
    GET  /properties/<slug:slug>/reviews/  -> ওই property-র রিভিউ লিস্ট
    POST /properties/<slug:slug>/reviews/  -> ওই property-র জন্য নতুন রিভিউ (auth দরকার) but now used allow any
    """
    serializer_class = ReviewSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return (Review.objects
                .select_related("user", "property")
                .filter(property__slug=slug))

    # def perform_create(self, serializer):
    #     prop = get_object_or_404(Property, slug=self.kwargs["slug"])
    #     serializer.save(user=self.request.user, property=prop)

    def perform_create(self, serializer):
        # real user না থাকলে default user assign করো
        user = self.request.user if self.request.user.is_authenticated else User.objects.first()
        prop_slug = self.kwargs["slug"]
        from apps.property.models import Property
        prop = Property.objects.get(slug=prop_slug)
        serializer.save(user=user, property=prop)
