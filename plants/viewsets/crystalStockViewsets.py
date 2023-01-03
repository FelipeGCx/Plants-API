from plants.models.crystalStock import CrystalStock
from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination
from plants.serializers.crystalStockSerializer import CrystalStockSerializer
import plants.rolePermission as rolePermision

class MyPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

class CrystalStockViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = CrystalStock.objects.all()
    serializer_class = CrystalStockSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]