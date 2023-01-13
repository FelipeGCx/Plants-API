from plants.models.plant import Plant
from plants.models.plantStock import PlantStock
from plants.serializers.plantStockSerializer import PlantStockSerializer
from plants.serializers.plantSerializer import PlantSerializer
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from django.shortcuts import get_object_or_404
import plants.rolePermission as rolePermision

class MyPagination(PageNumberPagination):
    page_size = 30
    page_size_query_param = 'page_size'
    max_page_size = 100

class PlantStockViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = PlantStock.objects.all()
    serializer_class = PlantStockSerializer

    def get_permissions(self):
        if self.action in ['create', 'update','destroy']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    lookup_field = 'param'
        
    def retrieve(self, request, param=None):
        queryset = PlantStock.objects.all()
        if param.isnumeric():
            plant = get_object_or_404(queryset, id=param)
        else:
            plant = get_object_or_404(queryset, name=param)
        serializer = PlantStockSerializer(plant)
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
        
        return  queryset
    
  