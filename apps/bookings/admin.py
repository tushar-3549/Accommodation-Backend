from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ("code", "property", "room_type", "rate_plan", "check_in", "check_out", "currency", "status", "created_at")
    list_filter = ("status", "currency", "check_in", "check_out")
    search_fields = ("code", "property__name", "user__username")
    ordering = ("-created_at",)
