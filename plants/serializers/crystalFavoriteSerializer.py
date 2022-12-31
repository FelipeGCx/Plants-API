from rest_framework import serializers
from plants.models.crystalFavorite import CystalFavorite

class CystalFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model= CystalFavorite
        fields = ["id","id_user","id_crystal"]
        
    def to_representation(self, obj):
        crystalFavorite = CystalFavorite.objects.get(id=obj.id)
        return {
            "id_user": crystalFavorite.id_user,
            "id_crystal": crystalFavorite.id_crystal,
        }