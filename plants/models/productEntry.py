from django.db import models
from plants.models.plantStock import PlantStock

# Create your models here.

class ProductEntry(models.Model):
     id_plant = models.ForeignKey(PlantStock, on_delete=models.CASCADE, default="")
     quantity = models.IntegerField()
     cost = models.BigIntegerField()
     
     