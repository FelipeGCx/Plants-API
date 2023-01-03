from plants.models.crystalFavorite import CrystalFavorite
from rest_framework import viewsets, permissions
from plants.serializers.crystalFavoriteSerializer import CrystalFavoriteSerializer
from django.shortcuts import get_object_or_404
import plants.rolePermission as rolePermision
from rest_framework.response import Response

class CrystalFavoriteViewSet(viewsets.ModelViewSet):
    queryset = CrystalFavorite.objects.all()
    serializer_class = CrystalFavoriteSerializer

    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
     
    def get_queryset(self):
        queryset = CrystalFavorite.objects.all()
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(id_user = user)
        return queryset