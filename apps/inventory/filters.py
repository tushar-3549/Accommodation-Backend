import django_filters
from .models import NightlyPrice, NightlyInventory

class NightlyPriceFilter(django_filters.FilterSet):
    stay_date = django_filters.DateFromToRangeFilter()
    class Meta:
        model = NightlyPrice
        fields = ["property", "room_type", "rate_plan", "currency", "stay_date"]

class NightlyInventoryFilter(django_filters.FilterSet):
    stay_date = django_filters.DateFromToRangeFilter()
    class Meta:
        model = NightlyInventory
        fields = ["property", "room_type", "stay_date"]
