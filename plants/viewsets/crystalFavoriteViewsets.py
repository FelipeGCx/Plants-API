from plants.models.crystalFavorite import CystalFavorite
from rest_framework import viewsets, permissions
from plants.serializers.crystalFavoriteSerializer import CystalFavoriteSerializer
import plants.rolePermission as rolePermision

class CrystalFavoriteViewSet(viewsets.ModelViewSet):
    queryset = CystalFavorite.objects.all()
    serializer_class = CystalFavoriteSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
