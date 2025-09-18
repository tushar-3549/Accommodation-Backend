# from rest_framework.routers import DefaultRouter
# from .views import PropertyViewSet, RoomTypeViewSet, RatePlanViewSet

# router = DefaultRouter()
# router.register(r"", PropertyViewSet, basename="property")                 # /properties/
# router.register(r"room-types", RoomTypeViewSet, basename="roomtype")      # /properties/room-types/
# router.register(r"rate-plans", RatePlanViewSet, basename="rateplan")      # /properties/rate-plans/

# urlpatterns = router.urls


from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, RoomTypeViewSet, RatePlanViewSet

router = DefaultRouter()
router.register(r"", PropertyViewSet, basename="property")  # /properties/

urlpatterns = [
    path("room-types/", RoomTypeViewSet.as_view({"get": "list", "post": "create"}), name="roomtype-list"),
    path("room-types/<int:pk>/", RoomTypeViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="roomtype-detail"),

    path("rate-plans/", RatePlanViewSet.as_view({"get": "list", "post": "create"}), name="rateplan-list"),
    path("rate-plans/<int:pk>/", RatePlanViewSet.as_view({"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}), name="rateplan-detail"),
]

urlpatterns += router.urls
