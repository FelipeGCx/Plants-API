from rest_framework import serializers
from plants.models.productOrder import ProductOrder

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ["id", "id_plant", "id_crystal", "id_user", "id_pot", "gift"]
        
    def tp_representatio(self, obj):
        orden = ProductOrder.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "id_plant": orden.id_plant, 
            "id_crystal": orden.id_crystal, 
            "id_user": orden.id_user, 
            "id_pot": orden.id_pot, 
            "gift": orden.gift, 
        }