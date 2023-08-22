from rest_framework import serializers
from plants.models.crystal import Crystal

class CrystalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Crystal
        fields = "__all__"
        
    def to_representation(self, obj):
        crystal = Crystal.objects.get(id=obj.id)
        return {
            "id": crystal.id,
            "name": crystal.name,
            "description": crystal.description,
            "vibration": crystal.vibration,
            "benefits": [b.removeprefix(" ") for b in crystal.benefits.split(",")],
            "properties": [p.removeprefix(" ") for p in crystal.properties.split(",")],
            "zodiac": [z.removeprefix(" ") for z in crystal.zodiac.split(",")],
            "planets": [p.removeprefix(" ") for p in crystal.planets.split(",")],
            "elements": [e.removeprefix(" ") for e in crystal.elements.split(",")],
            "chakras": [c.removeprefix(" ") for c in crystal.chakras.split(",")],
            "imageCrystal": crystal.image_crystal,
            "imageGemstone": crystal.image_gemstone
        }
            
        