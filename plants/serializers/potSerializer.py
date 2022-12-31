from rest_framework import serializers
from plants.models.pot import Pot

class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ["id", "name", "price", "image", "quantity"]
        
    def tp_representatio(self, obj):
        orden = Pot.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "name": orden.name, 
            "price": orden.price, 
            "image": orden.image, 
            "quantity": orden.quantity, 
        }