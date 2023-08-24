from rest_framework import serializers
from plants.models import CrystalStock
from plants.models import CrystalFavorite
from plants.serializers import CrystalSerializer

class CrystalStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrystalStock
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        id_user = self.context.get('id_user')
        favorite = CrystalFavorite.objects.filter(id_user=id_user, id_crystal=rep['id_crystal'] )
        rep.update({'favorite':favorite})
        crystal_rep = CrystalSerializer(instance.id_crystal).data
        rep.update(crystal_rep)
        rep.pop('id_crystal', None)
        return rep
