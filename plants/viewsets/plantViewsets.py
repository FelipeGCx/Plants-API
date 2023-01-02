from django.shortcuts import get_object_or_404
from plants.models.plant import Plant
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from plants.serializers.plantSerializer import PlantSerializer
import plants.rolePermission as rolePermision

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    lookup_field = 'param'
    
    def retrieve(self, request, param=None):
        queryset = Plant.objects.all()
        if param.isnumeric():
            crystal = get_object_or_404(queryset, id=param)
        else:
            crystal = get_object_or_404(queryset, name=param)
        serializer = PlantSerializer(crystal)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Plant.objects.all()

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__contains = name) or queryset.filter(other_names__contains = name) 
            
        species = self.request.query_params.get('species', None)
        if species is not None:
            queryset = queryset.filter(species = species) 
            
        group = self.request.query_params.get('group', None)
        if group is not None:
            queryset = queryset.filter(group = group) 
            
        flowering = self.request.query_params.get('flowering', None)
        if flowering is not None:
            queryset = queryset.filter(flowering = flowering) 
        
        return queryset
    
