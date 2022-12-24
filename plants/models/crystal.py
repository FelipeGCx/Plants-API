from django.db import models
# Create your models here.

class Crystal(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(default="")
    vibration = models.IntegerField(default=0)
    benefits =   models.TextField(default="")
    properties =  models.TextField(default="")
    zodiac = models.TextField(default="")
    planets =  models.TextField(default="")
    elements =  models.TextField(default="")
    chakras =   models.TextField(default="")
    image_crystal = models.TextField(default="")
    image_gemstone = models.TextField(default="")