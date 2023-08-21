from plants.filters import PlantStockFilter
from plants.models import PlantStock
from plants.models import User
from plants.serializers import PlantStockFavSerializer
from plants.utils import MyPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
import plants.rolePermission as rolePermision
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


class PlantStockFavView(ListAPIView):
    queryset = PlantStock.objects.all()
    serializer_class = PlantStockFavSerializer
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = PlantStockFilter

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            permission_classes = [
                permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        id_user = kwargs['pk']
        try:
            user = User.objects.get(id=id_user)
        except:
            return Response(None, 404)

        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
        
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(
                page, many=True, context={'id_user': id_user})
            if len(serializer.data) > 0:
                results = self.get_paginated_response(serializer.data)
                return Response(results)

        return Response(None, 404)

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.list(request, *args, **kwargs)
