from plants.models.poToOs import ProductOrderToOrderSale
from rest_framework import viewsets, permissions
from plants.serializers.poToOsSerializer import ProductOrderToOrderSaleSerializer

class ProductOrderToOrderSaleViewSet(viewsets.ModelViewSet):
    queryset = ProductOrderToOrderSale.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductOrderToOrderSaleSerializer
    