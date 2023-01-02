from plants.models.productOrder import ProductOrder
from rest_framework import viewsets, permissions
from plants.serializers.productOrderSerializer import ProductOrderSerializer
import plants.rolePermission as rolePermision

class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]