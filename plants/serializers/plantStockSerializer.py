from rest_framework import serializers
from plants.models.plant import Plant
from plants.models.plantStock import PlantStock
from plants.serializers.plantSerializer import PlantSerializer

class PlantStockSerializer(serializers.ModelSerializer):
    class Meta:
        model= PlantStock
        fields = ["id","id_plant", "quantity", "price", "discount","state"]
        
    def get_plant(self, obj):
        id_plant = int(str(obj.id).replace("Plant object (","").replace(")","")) 
        plants = Plant.objects.get(id=id_plant)
        serializer = PlantSerializer(plants, many=False)
        return serializer.data
        
    def to_representation(self, obj):
        plantStock = PlantStock.objects.get(id=obj.id)
        return {
            "id": plantStock.id,
            "plant": self.get_plant(obj),
            "quantity": plantStock.quantity,
            "price": plantStock.price,
            "discount": plantStock.discount,
            "state": plantStock.state
        }
        
# class PlantStockSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= PlantStock
#         fields = ["id","id_plant", "quantity", "price", "discount","state"]
        
#     class Meta:
#         model= Plant
#         fields = ["id","name","other_names","description","species","group","light","irrigation","temperature","precautions","flowering","size","image_front","render","created_at","inside"]
#         read_only_field = ("created_at",)
        
#     def to_representation(self, obj):
#         plantStock = PlantStock.objects.get(id=obj.id)
#         plant = Plant.objects.get(id=obj.id)
#         return {
#             "id": plant.id,
#             "name": plant.name,
#             "otherNames": [n.removeprefix(" ") for n in plant.other_names.split(",")],
#             "description": plant.description,
#             "species": plant.species,
#             "group": plant.group,
#             "light": [l.removeprefix(" ") for l in plant.light.split(",")],
#             "irrigation": plant.irrigation,
#             "temperature": plant.temperature,
#             "precautions": [p.removeprefix(" ") for p in plant.precautions.split(",")],
#             "flowering": plant.flowering,
#             "size": plant.size,
#             "imageFront": plant.image_front,
#             "render": plant.render,
#             "inside": plant.inside,
#             "quantity": plantStock.quantity,
#             "price": plantStock.price,
#             "discount": plantStock.discount,
#             "createdAt": plant.created_at,
#             "state": plantStock.state
#         }