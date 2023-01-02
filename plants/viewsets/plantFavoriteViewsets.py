from plants.models.plantFavorite import PlantFavorite
from rest_framework import viewsets, permissions
from plants.serializers.plantFavoriteSerializer import PlantFavoriteSerializer
import plants.rolePermission as rolePermision

class PlantFavoriteViewSet(viewsets.ModelViewSet):
    queryset = PlantFavorite.objects.all()
    serializer_class = PlantFavoriteSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]