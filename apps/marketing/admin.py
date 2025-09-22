from django.contrib import admin
from .models import Promotion, Campaign, Banner, FeaturedCollection, CollectionItem

@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ("name", "badge_text", "start_at", "end_at")
    search_fields = ("name",)

@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "start_at", "end_at")
    search_fields = ("name", "slug")

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "placement", "order", "active")
    list_filter = ("placement", "active")
    search_fields = ("title",)

class CollectionItemInline(admin.TabularInline):
    model = CollectionItem
    extra = 0

@admin.register(FeaturedCollection)
class FeaturedCollectionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "order", "active")
    search_fields = ("title", "slug")
    inlines = [CollectionItemInline]
