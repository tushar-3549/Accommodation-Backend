from rest_framework.routers import DefaultRouter
from .views import PropertyViewSet, RoomTypeViewSet, RatePlanViewSet

router = DefaultRouter()
router.register(r"", PropertyViewSet, basename="property")                 # /properties/
router.register(r"room-types", RoomTypeViewSet, basename="roomtype")      # /properties/room-types/
router.register(r"rate-plans", RatePlanViewSet, basename="rateplan")      # /properties/rate-plans/

urlpatterns = router.urls
