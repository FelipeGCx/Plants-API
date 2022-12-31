from plants.models.pot import Pot
from rest_framework import viewsets, permissions
from plants.serializers.potSerializer import PotSerializer

class PotViewSet(viewsets.ModelViewSet):
    queryset = Pot.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PotSerializer
    