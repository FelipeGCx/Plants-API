from plants.models.peToOp import ProductEntryToOrderPurchase
from rest_framework import viewsets, permissions
from plants.serializers.peToOpSerializer import ProductEntryToOrderPurchaseSerializer
import plants.rolePermission as rolePermision

class ProductEntryToOrderPurchaseViewSet(viewsets.ModelViewSet):
    queryset = ProductEntryToOrderPurchase.objects.all()
    serializer_class = ProductEntryToOrderPurchaseSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]