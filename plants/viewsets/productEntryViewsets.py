from plants.models.productEntry import ProductEntry
from rest_framework import viewsets, permissions
from plants.serializers.productEntrySerializer import ProductEntrySerializer
import plants.rolePermission as rolePermision

class ProductEntryViewSet(viewsets.ModelViewSet):
    queryset = ProductEntry.objects.all()
    serializer_class = ProductEntrySerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update', 'list','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]