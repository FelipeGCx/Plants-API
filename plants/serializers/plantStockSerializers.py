from rest_framework import serializers
from plants.models.plantStock import PlantStock

class PlantStockSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlantStock
        fields = ["id","id_plant", "quantity", "price", "discount","state"]
        
    def to_representation(self, obj):
        plantStock = PlantStock.objects.get(id=obj.id)
        return {
            "id": plantStock.id,
            "id_plant": plantStock.id_plant,
            "quantity": plantStock.quantity,
            "price": plantStock.price,
            "discount": plantStock.discount,
            "state": plantStock.state
        }