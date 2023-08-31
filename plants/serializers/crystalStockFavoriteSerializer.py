from rest_framework import serializers
from plants.models import CrystalFavorite
from plants.serializers import CrystalStockSerializer

class CrystalStockFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CrystalFavorite
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        crystal_rep = CrystalStockSerializer(instance.id_crystal).data
        rep.update(crystal_rep)
        rep.pop('id_user', None)
        rep.pop('id_crystal', None)
        return rep
