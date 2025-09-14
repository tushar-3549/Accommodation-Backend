from rest_framework.routers import DefaultRouter
from .views import ShortCardViewSet

router = DefaultRouter()
router.register(r"short-cards", ShortCardViewSet, basename="shortcard")
urlpatterns = router.urls
