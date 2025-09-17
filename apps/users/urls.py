from rest_framework.routers import DefaultRouter
from .views import UserViewSet


from django.urls import path
from .views import MeProfileView, MeSummaryView


router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
urlpatterns = router.urls


urlpatterns += [
    path("me/profile", MeProfileView.as_view()),
    path("me/summary", MeSummaryView.as_view()),
]

