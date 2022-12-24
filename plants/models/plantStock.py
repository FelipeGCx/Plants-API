from django.db import models
from plants.models.plant import Plant
# Create your models here.

class PlantStock(models.Model):
    id_plant = models.ForeignKey(Plant, on_delete=models.CASCADE, default="")
    quantity = models.IntegerField(default=0)
    price = models.BigIntegerField(default=0)
    discount = models.IntegerField(default=0)
    state = models.BooleanField(default=True)