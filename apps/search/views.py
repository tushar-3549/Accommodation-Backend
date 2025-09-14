from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter
from .models import SearchSuggestion
from .serializers import SearchSuggestionSerializer

class SuggestionListView(ListAPIView):
    queryset = SearchSuggestion.objects.all()
    serializer_class = SearchSuggestionSerializer
    filter_backends = [SearchFilter]
    search_fields = ["display"]
