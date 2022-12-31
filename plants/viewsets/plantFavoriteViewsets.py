from plants.models.plantFavorite import PlantFavorite
from rest_framework import viewsets, permissions
from plants.serializers.plantFavoriteSerializer import PlantFavoriteSerializer

class PlantFavoriteViewSet(viewsets.ModelViewSet):
    queryset = PlantFavorite.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlantFavoriteSerializer