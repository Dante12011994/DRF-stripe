import stripe
from django.conf import settings
from rest_framework.generics import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Item
from shop.serializers import ItemSerializer


class ItemView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item.html'

    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        serializer = ItemSerializer(item)
        return Response({'item': serializer.data, 'api_key': settings.STRIPE_API_KEY})


class BuyView(APIView):

    def get(self, request, pk):
        stripe.api_key = settings.STRIPE_API_KEY

        item = get_object_or_404(Item, pk=pk)
        price = stripe.Price.create(
            currency="usd",
            unit_amount=item.price,
            product_data={"name": item.name},
        )
        session = stripe.checkout.Session.create(
            success_url="http://127.0.0.1:8000",
            line_items=[{"price": price['id'], "quantity": 1}],
            mode="payment",
        )
        return Response({'id': session.id})
