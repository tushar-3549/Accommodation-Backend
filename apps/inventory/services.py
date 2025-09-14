from decimal import Decimal

def compute_final_price(base: Decimal, discount_percent: int) -> Decimal:
    if discount_percent <= 0:
        return base
    return (base * (Decimal(100 - discount_percent) / Decimal(100))).quantize(Decimal("0.01"))
