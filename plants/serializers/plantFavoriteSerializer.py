from rest_framework import serializers
from plants.models.plant import Plant
from plants.models.plantFavorite import PlantFavorite
from plants.serializers.plantSerializer import PlantSerializer

class PlantFavoriteSerializer(serializers.ModelSerializer):
    plant  =  serializers.SerializerMethodField()
    class Meta:
        model= PlantFavorite
        fields = ["id","id_user","id_plant","plant"]
        
    def get_plant(self, obj):
        id_plant = int(str(obj.id_plant).replace("PlantStock object (","").replace(")","")) 
        plants = Plant.objects.get(id=id_plant)
        serializer = PlantSerializer(plants, many=False)
        return serializer.data