from rest_framework import serializers

from .models import Item


class ItemRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = ('id', )


class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        exclude = ('id', 'date')

