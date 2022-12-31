from plants.models.orderSale import OrderSale
from rest_framework import viewsets, permissions
from plants.serializers.orderSaleSerializer import OrderSaleSerializer

class OrderSaleViewSet(viewsets.ModelViewSet):
    queryset = OrderSale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderSaleSerializer
    