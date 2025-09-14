import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    city = django_filters.NumberFilter(field_name="city_id")
    category = django_filters.CharFilter(field_name="category")
    is_featured = django_filters.BooleanFilter(field_name="is_featured")

    class Meta:
        model = Property
        fields = ["city", "category", "is_featured"]
