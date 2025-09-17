from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet, LandmarkViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet, basename="country")
router.register(r"cities", CityViewSet, basename="city")
router.register(r"landmarks", LandmarkViewSet, basename="landmark")
urlpatterns = router.urls
