from django.contrib import admin
from .models import NightlyPrice, NightlyInventory

@admin.register(NightlyPrice)
class NightlyPriceAdmin(admin.ModelAdmin):
    list_display = ("property", "room_type", "rate_plan", "stay_date", "currency", "base_price", "final_price", "discount_percent")
    list_filter = ("currency", "stay_date", "property")
    search_fields = ("property__name", "room_type__name", "rate_plan__name")
    ordering = ("stay_date",)

@admin.register(NightlyInventory)
class NightlyInventoryAdmin(admin.ModelAdmin):
    list_display = ("property", "room_type", "stay_date", "allotment")
    list_filter = ("stay_date", "property")
    search_fields = ("property__name", "room_type__name")
    ordering = ("stay_date",)
