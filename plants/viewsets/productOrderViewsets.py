from plants.models.productOrder import ProductOrder
from rest_framework import viewsets, permissions
from plants.serializers.productOrderSerializer import ProductOrderSerializer

class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductOrderSerializer
    