from django.urls import path

from shop.apps import ShopConfig
from shop.views import ItemView, BuyView

app_name = ShopConfig.name

urlpatterns = [
    path('item/<int:pk>/', ItemView.as_view(), name='item_view'),
    path('buy/<int:pk>/', BuyView.as_view(), name='buy_view'),
]
