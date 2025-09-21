from django.contrib import admin
from .models import SearchSuggestion

@admin.register(SearchSuggestion)
class SearchSuggestionAdmin(admin.ModelAdmin):
    list_display = ("id", "entity_type", "display", "ref_id")
    search_fields = ("display",)
    list_filter = ("entity_type",)
