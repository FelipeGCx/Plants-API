from rest_framework import serializers
from plants.models import PlantStock
from plants.models import PlantFavorite
from plants.serializers import PlantSerializer


class PlantStockFavSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantStock
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        id_user = self.context.get('id_user')
        favorite = PlantFavorite.objects.filter(id_user=id_user, id_plant=rep['id_plant']).exists()
        rep.update({'favorite':favorite})
        plant_rep = PlantSerializer(instance.id_plant).data
        rep.update(plant_rep)
        rep.pop('id_plant', None)
        return rep
