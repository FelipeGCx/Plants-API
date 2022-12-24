from plants.models.crystalStock import CrystalStock
from rest_framework import viewsets, permissions
from plants.serializers.crystalStockSerializers import CrystalStockSerializer

class CrystalStockViewSet(viewsets.ModelViewSet):
    queryset = CrystalStock.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CrystalStockSerializer
    