# from rest_framework import serializers
from plants.models.user import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields = ["id","email","password","image", "roles"]
        
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        return {
            "id": user.id,
            "email": user.email,
            "password": user.password,
            "image": user.image,
            "roles": [r.removeprefix(" ") for r in user.roles.split(",")],
        }