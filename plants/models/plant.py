from django.db import models
# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=210)
    other_names = models.TextField(default="")
    description = models.TextField(default="")
    species = models.CharField(max_length=200, default="Other")
    group = models.CharField(max_length=200,default="Succulent")
    light = models.TextField(default="")
    irrigation = models.CharField(max_length=200, default="")
    temperature = models.CharField(max_length=200, default="")
    precautions = models.TextField(default="")
    flowering = models.BooleanField(default=False)
    size = models.CharField(max_length=200,default="")
    image_front = models.TextField(default="")
    render = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True)
    zone = models.TextField(default="inside")