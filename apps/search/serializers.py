from rest_framework import serializers
from .models import SearchSuggestion

class SearchSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchSuggestion
        fields = ["id", "entity_type", "display", "ref_id", "extra"]
