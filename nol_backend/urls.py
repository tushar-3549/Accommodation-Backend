from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/jwt/create", TokenObtainPairView.as_view(), name="jwt-create"),
    path("auth/jwt/refresh", TokenRefreshView.as_view(), name="jwt-refresh"),

    path("geo/", include("apps.geo.urls")),
    path("search/", include("apps.search.urls")),
    path("inventory/", include("apps.inventory.urls")),
    path("properties/", include("apps.property.urls")),
    path("marketing/", include("apps.marketing.urls")),
    path("content/", include("apps.content.urls")),

    path("home/", include("apps.home.urls")),
    path("", include("apps.reviews.urls")),
    path("", include("apps.bookings.urls")),
    path("", include("apps.payments.urls")),


]
