from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Min, Value
from django.db.models.functions import Coalesce
from apps.property.models import Property
from apps.inventory.models import NightlyPrice
from apps.property.serializers import PropertyCardSerializer

class RecommendedView(APIView):
    def get(self, request):
        city_id = request.query_params.get("city")
        limit = int(request.query_params.get("limit", 10))
        currency = request.query_params.get("currency", "KRW")

        qs = Property.objects.select_related("city","city__country").prefetch_related("media")
        if city_id: qs = qs.filter(city_id=city_id)
        qs = qs.filter(is_featured=True)

        prices = NightlyPrice.objects.filter(property_id__in=qs.values("id"), currency=currency)
        qs = qs.annotate(
            min_price=Coalesce(Min("prices__final_price"), Value(0)),
        )

        data = PropertyCardSerializer(qs[:limit], many=True).data
        # inject currency (serializer min_price already added, ensure currency field)
        for d in data: d["currency"] = currency
        return Response(data)
