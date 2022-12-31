from plants.models.plantStock import PlantStock
from rest_framework import viewsets, permissions
from plants.serializers.plantStockSerializer import PlantStockSerializer

class PlantStockViewSet(viewsets.ModelViewSet):
    queryset = PlantStock.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlantStockSerializer