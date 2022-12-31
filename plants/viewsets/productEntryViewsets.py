from plants.models.productEntry import ProductEntry
from rest_framework import viewsets, permissions
from plants.serializers.productEntrySerializer import ProductEntrySerializer

class ProductEntryViewSet(viewsets.ModelViewSet):
    queryset = ProductEntry.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductEntrySerializer
    