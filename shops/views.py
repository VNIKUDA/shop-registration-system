from rest_framework import generics
from django.db.models import FloatField, F
from django.db.models import ExpressionWrapper, Func
from shops.models import Shop
from shops.serializers import ShopSerializer
import math

def haversine(lat1, lon1, lat2, lon2):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # Haversine formula
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = (math.sin(dlat / 2) ** 2 +
         math.cos(lat1_rad) * math.cos(lat2_rad) * (math.sin(dlon / 2) ** 2))
    c = 2 * math.asin(math.sqrt(a))
    R = 6371
    distance = R * c

    return distance

class ShopRegister(generics.CreateAPIView):
    serializer_class = ShopSerializer


class UserSearch(generics.ListAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        user_latitude = float(self.request.GET.get("latitude"))
        user_longitude = float(self.request.GET.get("longitude"))

        self.queryset = Shop.objects.all()

        if user_latitude and user_longitude:
            for shop in self.queryset:
                shop.distance = haversine(user_latitude, user_longitude, shop.latitude, shop.longitude)

            self.queryset = sorted(self.queryset, key=lambda shop: shop.distance)

        return self.queryset