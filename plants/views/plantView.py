from plants.filters.plantFilter import PlantFilter
from plants.models.plant import Plant
from plants.serializers.plantSerializer import PlantSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
import plants.rolePermission as rolePermision
from rest_framework import permissions
from plants.utils.pagination import MyPagination
from django_filters.rest_framework import DjangoFilterBackend


class PlantView(ListAPIView, RetrieveAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantFilter

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            permission_classes = [
                permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(page, many=True)
            if len(serializer.data) > 0:
                results = self.get_paginated_response(serializer.data)
                return Response(results)
        return Response(None, 404)
        
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
