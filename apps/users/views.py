from rest_framework import viewsets, permissions
from .models import User
from .serializers import UserSerializer

from rest_framework import permissions, views
from rest_framework.response import Response


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class MeProfileView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        u = request.user
        return Response({"id":u.id,"username":u.username,"email":u.email,"role":getattr(u,"role","CUSTOMER")})
    def patch(self, request):
        u = request.user
        for f in ["email", "first_name", "last_name"]:
            if f in request.data: setattr(u, f, request.data[f])
        u.save()
        return Response({"ok":True})

class MeSummaryView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        # Stubs; wire to your wallet/coupon if you add later
        return Response({"bookings_count": request.user.bookings.count(), "reviews_count": request.user.review_set.count(), "points": 0, "coupons": 0})
