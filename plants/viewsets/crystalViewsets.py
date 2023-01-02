from django.shortcuts import get_object_or_404
from plants.models.crystal import Crystal
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from plants.serializers.crystalSerializer import CrystalSerializer
import plants.rolePermission as rolePermision

class CrystalViewSet(viewsets.ModelViewSet):
    queryset = Crystal.objects.all()
    serializer_class = CrystalSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'update']:
            permission_classes = [permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]
    
    lookup_field = 'param'
    
    def retrieve(self, request, param=None):
        queryset = Crystal.objects.all()
        if param.isnumeric():
            crystal = get_object_or_404(queryset, id=param)
        else:
            crystal = get_object_or_404(queryset, name=param)
        serializer = CrystalSerializer(crystal)
        return Response(serializer.data)
    
    def get_queryset(self):
        queryset = Crystal.objects.all()

        name = self.request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__contains = name) 
            
        vibration = self.request.query_params.get('vibration', None)
        if vibration is not None:
            queryset = queryset.filter(vibration = vibration) 
            
        zodiac = self.request.query_params.get('zodiac', None)
        if zodiac is not None:
            zodiac = zodiac.split(",")
            for z in zodiac:
                queryset =  queryset.filter(zodiac__contains=z)
        
        planets = self.request.query_params.get('planets', None)
        if planets is not None:
            planets = planets.split(",")
            for p in planets:
                queryset =  queryset.filter(planets__contains=p)
                
        chakras = self.request.query_params.get('chakras', None)
        if chakras is not None:
            chakras = chakras.split(",")
            for c in chakras:
                queryset =  queryset.filter(chakras__contains=c)
                
        elements = self.request.query_params.get('elements', None)
        if elements is not None:
            elements = elements.split(",")
            for e in elements:
                queryset =  queryset.filter(elements__contains=e)
                
        return queryset
    
