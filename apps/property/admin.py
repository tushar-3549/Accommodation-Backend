from django.contrib import admin
from .models import Amenity, Property, Media, RoomType, RatePlan

@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)

class MediaInline(admin.TabularInline):
    model = Media
    extra = 1

class RoomTypeInline(admin.TabularInline):
    model = RoomType
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "category", "star_rating", "is_featured")
    list_filter = ("city", "category", "is_featured")
    search_fields = ("name", "city__name")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [MediaInline, RoomTypeInline]

@admin.register(RoomType)
class RoomTypeAdmin(admin.ModelAdmin):
    list_display = ("name", "property", "capacity_adults", "capacity_children")
    list_filter = ("property",)
    search_fields = ("name", "property__name")

@admin.register(RatePlan)
class RatePlanAdmin(admin.ModelAdmin):
    list_display = ("name", "room_type", "refundable")
    list_filter = ("refundable", "room_type")
    search_fields = ("name", "room_type__name")
