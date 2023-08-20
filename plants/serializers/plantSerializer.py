from rest_framework import serializers
from plants.models.plant import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model= Plant
        fields = ["__all__"]
        read_only_field = ("created_at",)
        
    def to_representation(self, obj):
        plant = Plant.objects.get(id=obj.id)
        return {
            'id': plant.id,
            "name": plant.name,
            "otherNames": [n.removeprefix(" ") for n in plant.other_names.split(",")],
            "description": plant.description,
            "species": plant.species,
            "group": plant.group,
            "light": [l.removeprefix(" ") for l in plant.light.split(",")],
            "irrigation": plant.irrigation,
            "temperature": plant.temperature,
            "precautions": [p.removeprefix(" ") for p in plant.precautions.split(",")],
            "flowering": plant.flowering,
            "size": plant.size,
            "imageFront": plant.image_front,
            "render": plant.render,
            "createdAt": plant.created_at,
            "zone": plant.zone
        }