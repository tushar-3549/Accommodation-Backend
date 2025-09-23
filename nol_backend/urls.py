from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="My API",
      default_version='v1',
      description="Test API documentation with Swagger",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="youremail@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)




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




    # Swagger UI
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),



]
