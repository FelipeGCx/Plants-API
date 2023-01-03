from django.db import models
from plants.models.crystalStock import CrystalStock
from plants.models.user import User
# Create your models here.

class CrystalFavorite(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    id_crystal = models.ForeignKey(CrystalStock, on_delete=models.CASCADE,default="")
    