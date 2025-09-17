from django.urls import path
from .views import RecommendedView

urlpatterns = [
    path("recommended/", RecommendedView.as_view(), name="recommended"),
]
