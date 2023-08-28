from rest_framework import serializers
from plants.models import PlantFavorite
from plants.serializers import PlantStockSerializer


class PlantStockFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantFavorite
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        plant_rep = PlantStockSerializer(instance.id_plant).data
        rep.update(plant_rep)
        rep.pop('id_user', None)
        rep.pop('id_plant', None)
        return rep
