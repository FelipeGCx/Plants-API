from plants.models.orderPurchase import OrderPurchase
from rest_framework import viewsets, permissions
from plants.serializers.orderPurchaseSerializer import OrderPurchaseSerializer
import plants.rolePermission as rolePermision

class OrderPurchaseViewSet(viewsets.ModelViewSet):
    queryset = OrderPurchase.objects.all()
    serializer_class = OrderPurchaseSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]