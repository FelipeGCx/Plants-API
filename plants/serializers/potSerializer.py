from rest_framework import serializers
from plants.models.pot import Pot

class PotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pot
        fields = ["id", "name", "price", "image", "quantity"]