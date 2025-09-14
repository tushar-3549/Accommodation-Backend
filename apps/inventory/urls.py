from rest_framework.routers import DefaultRouter
from .views import NightlyPriceViewSet, NightlyInventoryViewSet

router = DefaultRouter()
router.register(r"nightly-prices", NightlyPriceViewSet)
router.register(r"nightly-inventories", NightlyInventoryViewSet)
urlpatterns = router.urls
