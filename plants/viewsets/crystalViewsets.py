from plants.models.crystal import Crystal
from rest_framework import viewsets, permissions
from plants.serializers.crystalSerializers import CrystalSerializer

class CrystalViewSet(viewsets.ModelViewSet):
    queryset = Crystal.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CrystalSerializer
    