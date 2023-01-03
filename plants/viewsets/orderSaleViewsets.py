from plants.models.orderSale import OrderSale
from rest_framework import viewsets, permissions
from plants.serializers.orderSaleSerializer import OrderSaleSerializer
import plants.rolePermission as rolePermision

class OrderSaleViewSet(viewsets.ModelViewSet):
    queryset = OrderSale.objects.all()
    serializer_class = OrderSaleSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]