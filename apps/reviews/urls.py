from django.urls import path
from .views import PropertyReviewListCreate
urlpatterns = [ path("properties/<slug:slug>/reviews", PropertyReviewListCreate.as_view()) ]
