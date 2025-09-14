from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CityViewSet, LandmarkViewSet

router = DefaultRouter()
router.register(r"countries", CountryViewSet)
router.register(r"cities", CityViewSet)
router.register(r"landmarks", LandmarkViewSet)
urlpatterns = router.urls
