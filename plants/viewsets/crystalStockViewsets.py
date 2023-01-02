from plants.models.crystalStock import CrystalStock
from rest_framework import viewsets, permissions
from plants.serializers.crystalStockSerializer import CrystalStockSerializer
import plants.rolePermission as rolePermision

class CrystalStockViewSet(viewsets.ModelViewSet):
    queryset = CrystalStock.objects.all()
    serializer_class = CrystalStockSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]