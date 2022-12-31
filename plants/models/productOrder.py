from django.db import models
from plants.models.plantStock import PlantStock
from plants.models.crystalStock import CrystalStock
from plants.models.pot import Pot
from plants.models.user import User

# Create your models here.

class ProductOrder(models.Model):
     id_plant = models.ForeignKey(PlantStock, on_delete=models.CASCADE, default="")
     id_crystal = models.ForeignKey(CrystalStock, on_delete=models.CASCADE,default="")
     id_user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
     id_pot = models.ForeignKey(Pot, on_delete=models.CASCADE,default="")
     gift = models.BooleanField(default=False)
     
     