from plants.models import PlantFavorite
from plants.models import User
from plants.serializers import PlantStockFavoriteSerializer
from plants.utils import MyPagination
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
import plants.rolePermission as rolePermision
from rest_framework import permissions


class PlantStockFavoriteView(ListAPIView):
    queryset = PlantFavorite.objects.all()
    serializer_class = PlantStockFavoriteSerializer
    pagination_class = MyPagination

    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE', 'PATCH']:
            permission_classes = [
                permissions.IsAuthenticated, rolePermision.IsAdmin]
        else:
            permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]

    def get_queryset(self):
        id_user = self.kwargs.get('pk')
        user = User.objects.get(id=id_user)

        queryset = PlantFavorite.objects.filter(id_user=user)
        return queryset.order_by('id')

    def list(self, request, *args, **kwargs):
        id_user = kwargs['pk']
        try:
            user = User.objects.get(id=id_user)
        except:
            return Response(None, 404)

        queryset = self.get_queryset().order_by('id')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.serializer_class(
                page, many=True)
            if len(serializer.data) > 0:
                results = self.get_paginated_response(serializer.data)
                return Response(results)

        return Response(None, 404)

    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            return self.list(request, *args, **kwargs)
