from django.db import models
from plants.models.crystal import Crystal
# Create your models here.

class CrystalStock(models.Model):
    id_crystal = models.ForeignKey(Crystal, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField(default=0)
    price = models.BigIntegerField(default=0)
    state = models.BooleanField(default=True)