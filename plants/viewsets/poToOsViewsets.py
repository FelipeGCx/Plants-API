from plants.models.poToOs import ProductOrderToOrderSale
from rest_framework import viewsets, permissions
from plants.serializers.poToOsSerializer import ProductOrderToOrderSaleSerializer
import plants.rolePermission as rolePermision

class ProductOrderToOrderSaleViewSet(viewsets.ModelViewSet):
    queryset = ProductOrderToOrderSale.objects.all()
    serializer_class = ProductOrderToOrderSaleSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]