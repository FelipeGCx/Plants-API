from django.db import models
from plants.models.plantStock import PlantStock
from plants.models.user import User
# Create your models here.

class PlantFavorite(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    id_plant = models.ForeignKey(PlantStock, on_delete=models.CASCADE, default="")
    