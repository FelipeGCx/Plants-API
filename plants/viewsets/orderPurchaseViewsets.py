from plants.models.orderPurchase import OrderPurchase
from rest_framework import viewsets, permissions
from plants.serializers.orderPurchaseSerializer import OrderPurchaseSerializer

class OrderPurchaseViewSet(viewsets.ModelViewSet):
    queryset = OrderPurchase.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = OrderPurchaseSerializer
    