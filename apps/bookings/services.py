from decimal import Decimal
from apps.inventory.models import NightlyPrice


def quote_total(property_id, room_type_id, rate_plan_id, check_in, check_out, currency="KRW"):
    nights = (check_out - check_in).days
    prices = (NightlyPrice.objects
              .filter(property_id=property_id, room_type_id=room_type_id, rate_plan_id=rate_plan_id,
                      currency=currency, stay_date__gte=check_in, stay_date__lt=check_out)
              .values_list("final_price", flat=True))
    subtotal = sum(prices) if prices else Decimal("0.00")
    taxes = (Decimal("0.10") * subtotal).quantize(Decimal("0.01"))  # 10% mock tax
    total = (subtotal + taxes).quantize(Decimal("0.01"))
    return {"nights": nights, "subtotal": str(subtotal), "taxes": str(taxes), "total": str(total)}
