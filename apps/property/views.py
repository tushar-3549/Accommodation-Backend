from datetime import date
from django.db.models import Min, F, Value, IntegerField
from django.db.models.functions import Coalesce
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Property
from .serializers import PropertyCardSerializer, PropertyDetailSerializer
from .filters import PropertyFilter
from apps.inventory.models import NightlyPrice

class PropertyViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Property.objects.select_related("city", "city__country").prefetch_related("media")
    filter_backends = [DjangoFilterBackend]
    filterset_class = PropertyFilter

    def get_serializer_class(self):
        return PropertyDetailSerializer if self.action == "retrieve" else PropertyCardSerializer

    def list(self, request, *args, **kwargs):
        qs = self.filter_queryset(self.get_queryset())

        # Search param (by property name or city name)
        query = request.query_params.get("query")
        if query:
            qs = qs.filter(name__icontains=query) | qs.filter(city__name__icontains=query)

        # Price join (optional window)
        check_in = request.query_params.get("check_in")
        check_out = request.query_params.get("check_out")
        currency = request.query_params.get("currency", "KRW")

        price_qs = NightlyPrice.objects.filter(property_id=F("property__id"), currency=currency)
        if check_in and check_out:
            price_qs = price_qs.filter(stay_date__gte=check_in, stay_date__lt=check_out)
        else:
            price_qs = price_qs.filter(stay_date__gte=date.today())

        qs = qs.annotate(
            min_price=Coalesce(Min(price_qs.values("final_price")), Value(0)),
            currency=Value(currency),
            discount_percent=Coalesce(Min(price_qs.values("discount_percent")), Value(0), output_field=IntegerField()),
        )

        page = self.paginate_queryset(qs)
        ser = self.get_serializer(page, many=True)
        return self.get_paginated_response(ser.data)

    @action(detail=True, methods=["get"])
    def availability(self, request, pk=None):
        prop = self.get_object()
        check_in = request.query_params.get("check_in")
        check_out = request.query_params.get("check_out")
        currency = request.query_params.get("currency", "KRW")
        if not (check_in and check_out):
            return Response({"detail": "check_in and check_out are required"}, status=400)

        prices = (NightlyPrice.objects
                  .filter(property=prop, currency=currency,
                          stay_date__gte=check_in, stay_date__lt=check_out)
                  .order_by("stay_date")
                  .values("stay_date", "base_price", "final_price", "discount_percent"))

        total = sum(p["final_price"] for p in prices) if prices else 0
        return Response({
            "property": prop.slug,
            "currency": currency,
            "nights": len(prices),
            "total_price": total,
            "nights_breakdown": list(prices),
        })
    
    @action(detail=False, methods=["get"], url_path="map")
    def on_map(self, request):
        bounds = request.query_params.get("bounds")  # "lat1,lng1,lat2,lng2"
        query = request.query_params.get("query")
        qs = self.filter_queryset(self.get_queryset())
        if query:
            qs = qs.filter(name__icontains=query) | qs.filter(city__name__icontains=query)
        if bounds:
            lat1,lng1,lat2,lng2 = [float(x) for x in bounds.split(",")]
            lo_lat, hi_lat = min(lat1,lat2), max(lat1,lat2)
            lo_lng, hi_lng = min(lng1,lng2), max(lng1,lng2)
            qs = qs.filter(latitude__gte=lo_lat, latitude__lte=hi_lat,
                           longitude__gte=lo_lng, longitude__lte=hi_lng)
        data = [
            {"id":p.id,"name":p.name,"slug":p.slug,"lat":float(p.latitude or 0),"lng":float(p.longitude or 0),
             "min_price":str(getattr(p,"min_price",0)),"currency":"KRW"}
            for p in qs[:200]
        ]
        return Response(data)




