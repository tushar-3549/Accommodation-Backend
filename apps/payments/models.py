import uuid
from decimal import Decimal
from rest_framework.views import APIView
from rest_framework.response import Response

class PaymentIntentView(APIView):
    def post(self, request):
        amount = Decimal(request.data["amount"])
        currency = request.data.get("currency", "KRW")
        provider = request.data.get("provider", "mock")
        client_secret = f"pi_{uuid.uuid4().hex}"
        return Response({"id": client_secret, "provider": provider, "amount": str(amount), "currency": currency, "status": "requires_confirmation"})
