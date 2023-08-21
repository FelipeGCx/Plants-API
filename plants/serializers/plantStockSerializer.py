from rest_framework import serializers
from plants.models import Plant
from plants.serializers import PlantSerializer
from plants.models import PlantStock

class PlantStockSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlantStock
        fields = "__all__"
        
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        plant_rep = PlantSerializer(instance.id_plant).data
        rep.update(plant_rep)
        rep.pop('id_plant', None)
        return rep