from rest_framework import serializers

from shop.models import Item


class ItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=250)
    description = serializers.CharField()
    price = serializers.IntegerField()


