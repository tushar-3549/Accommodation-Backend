from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .models import SearchSuggestion
from .serializers import SearchSuggestionSerializer

from rest_framework import filters

# class SuggestionListView(ListAPIView):
#     queryset = SearchSuggestion.objects.all()
#     serializer_class = SearchSuggestionSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ["display"]


class SuggestionListView(ListAPIView):
    queryset = SearchSuggestion.objects.all()
    serializer_class = SearchSuggestionSerializer
    filter_backends = [SearchFilter, filters.OrderingFilter]
    search_fields = ["display"]
    ordering_fields = ["entity_type", "display", "id"]
