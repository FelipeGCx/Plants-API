from rest_framework import serializers
from plants.models.productOrder import ProductOrder

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ["id", "id_plant", "id_crystal", "id_user", "id_pot", "gift"]