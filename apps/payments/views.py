# import uuid
# from decimal import Decimal
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class PaymentIntentView(APIView):
#     def post(self, request):
#         amount = Decimal(request.data["amount"])
#         currency = request.data.get("currency", "KRW")
#         provider = request.data.get("provider", "mock")

#         client_secret = f"pi_{uuid.uuid4().hex}"

#         return Response({
#             "id": client_secret,
#             "provider": provider,
#             "amount": str(amount),
#             "currency": currency,
#             "status": "requires_confirmation"
#         })






import uuid
from decimal import Decimal
from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from .models import Payment
from .serializers import PaymentSerializer

class PaymentIntentView(APIView):
    permission_classes = [permissions.AllowAny]  # dev-only; prod এ tighten করবে

    @transaction.atomic
    def post(self, request):
        # validate
        try:
            amount = Decimal(str(request.data["amount"]))
        except KeyError:
            return Response({"detail": "amount is required"}, status=400)
        except Exception:
            return Response({"detail": "amount must be a number"}, status=400)

        currency = request.data.get("currency", "KRW")
        provider = request.data.get("provider", "mock")
        booking_code = request.data.get("booking_code", "")

        client_secret = f"pi_{uuid.uuid4().hex}"

        pay = Payment.objects.create(
            amount=amount,
            currency=currency,
            provider=provider,
            client_secret=client_secret,
            booking_code=booking_code,
            status=Payment.Status.REQUIRES_CONFIRMATION,
        )
        return Response(PaymentSerializer(pay).data, status=201)


class PaymentConfirmView(APIView):
    """
    Mock 'confirm' endpoint: বাস্তবে এটা গেটওয়ে webhook করবে।
    """
    permission_classes = [permissions.AllowAny]

    @transaction.atomic
    def post(self, request, client_secret: str):
        try:
            pay = Payment.objects.select_for_update().get(client_secret=client_secret)
        except Payment.DoesNotExist:
            return Response({"detail": "payment not found"}, status=404)

        outcome = request.data.get("outcome", "succeeded")  # "succeeded"/"failed"/"canceled"
        if outcome not in ("succeeded", "failed", "canceled"):
            return Response({"detail": "invalid outcome"}, status=400)

        pay.status = outcome
        pay.save(update_fields=["status","updated_at"])
        return Response(PaymentSerializer(pay).data, status=200)
