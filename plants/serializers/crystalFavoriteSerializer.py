from rest_framework import serializers
from plants.models.crystal import Crystal
from plants.models.crystalFavorite import CrystalFavorite
from plants.serializers.crystalSerializer import CrystalSerializer

class CrystalFavoriteSerializer(serializers.ModelSerializer):
    crystal = serializers.SerializerMethodField()
    class Meta:
        model= CrystalFavorite
        fields = ["id","id_user","id_crystal","crystal"]
        
    def get_crystal(self, obj):
        id_crystal = int(str(obj.id_crystal).replace("CrystalStock object (","").replace(")","")) 
        crystals = Crystal.objects.get(id=id_crystal)
        serializer = CrystalSerializer(crystals, many=False)
        return serializer.data