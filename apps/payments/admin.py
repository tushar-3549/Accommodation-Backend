from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("client_secret", "amount", "currency", "status", "provider", "booking_code", "created_at", "updated_at")
    list_filter = ("status", "currency", "provider", "created_at")
    search_fields = ("client_secret", "booking_code", "user__username")
    ordering = ("-created_at",)
