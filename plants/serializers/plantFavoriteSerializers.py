from rest_framework import serializers
from plants.models.plantFavorite import PlantFavorite

class PlantFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlantFavorite
        fields = ["id","id_user","id_plant"]
        
    def to_representation(self, obj):
        plantFavorite = PlantFavorite.objects.get(id=obj.id)
        return {
            "id_user": plantFavorite.id_user,
            "id_plant": plantFavorite.id_plant,
        }