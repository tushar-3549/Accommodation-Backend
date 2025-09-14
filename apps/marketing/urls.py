from rest_framework.routers import DefaultRouter
from .views import PromotionViewSet, BannerViewSet, FeaturedCollectionViewSet

router = DefaultRouter()
router.register(r"promotions", PromotionViewSet, basename="promotion")
router.register(r"banners", BannerViewSet, basename="banner")
router.register(r"featured-collections", FeaturedCollectionViewSet, basename="featuredcollection")
urlpatterns = router.urls
