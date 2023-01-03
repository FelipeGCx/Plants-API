from plants.models.pot import Pot
from rest_framework import viewsets, permissions
from plants.serializers.potSerializer import PotSerializer
import plants.rolePermission as rolePermision

class PotViewSet(viewsets.ModelViewSet):
    queryset = Pot.objects.all()
    serializer_class = PotSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]