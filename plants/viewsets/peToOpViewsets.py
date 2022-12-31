from plants.models.peToOp import ProductEntryToOrderPurchase
from rest_framework import viewsets, permissions
from plants.serializers.peToOpSerializer import ProductEntryToOrderPurchaseSerializer

class ProductEntryToOrderPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ProductEntryToOrderPurchase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductEntryToOrderPurchaseSerializer
    