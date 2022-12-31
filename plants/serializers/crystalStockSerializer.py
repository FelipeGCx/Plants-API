from rest_framework import serializers
from plants.models.crystalStock import CrystalStock

class CrystalStockSerializer(serializers.ModelSerializer):
    class Meta:
        model= CrystalStock
        fields = ["id","id_crystal", "quantity", "price", "state"]
        
    # def to_representation(self, obj):
    #     crystalStock = CrystalStock.objects.get(id=obj.id)
    #     return {
    #         "id": crystalStock.id,
    #         "id_crystal": crystalStock.id_crystal,
    #         "quantity": crystalStock.quantity,
    #         "price": crystalStock.price,
    #         "state": crystalStock.state
    #     }