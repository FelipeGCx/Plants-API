from rest_framework import serializers
from plants.models.productEntry import ProductEntry

class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntry
        fields = ["id", "id_plant", "quantity", "cost"]