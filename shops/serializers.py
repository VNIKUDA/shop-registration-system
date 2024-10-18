from rest_framework import serializers
from shops.models import Shop


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'latitude', 'longitude']


    def to_representation(self, instance):
        data = super().to_representation(instance)

        if hasattr(instance, 'distance'):
            data["distance"] = instance.distance

        return data