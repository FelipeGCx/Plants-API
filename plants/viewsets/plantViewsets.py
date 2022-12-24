from plants.models.plant import Plant
from rest_framework import viewsets, permissions
from plants.serializers.plantSerializers import PlantSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PlantSerializer