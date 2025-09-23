from django.contrib import admin
from .models import ShortCard

@admin.register(ShortCard)
class ShortCardAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "locale", "media_type", "badge", "order", "active", "view_count", "created_at")
    list_filter = ("active", "section", "locale", "media_type")
    search_fields = ("title", "subtitle")
    ordering = ("order", "id")
