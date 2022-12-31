from plants.models.crystalFavorite import CystalFavorite
from rest_framework import viewsets, permissions
from plants.serializers.crystalFavoriteSerializer import CystalFavoriteSerializer

class CrystalFavoriteViewSet(viewsets.ModelViewSet):
    queryset = CystalFavorite.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CystalFavoriteSerializer
    