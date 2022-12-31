from rest_framework import serializers
from plants.models.productEntry import ProductEntry

class ProductEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntry
        fields = ["id", "id_plant", "quantity", "cost"]
        
    def tp_representatio(self, obj):
        orden = ProductEntry.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "id_plant": orden.id_plant, 
            "quantity": orden.quantity, 
            "cost": orden.cost, 
        }