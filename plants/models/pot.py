from django.db import models
# Create your models here.

class Pot(models.Model):
    name = models.CharField(max_length=210)
    price = models.BigIntegerField()
    image = models.TextField()
    size = models.TextField(default="")
    render = models.TextField()
    quantity = models.IntegerField()