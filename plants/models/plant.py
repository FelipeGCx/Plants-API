from django.db import models
# Create your models here.

class Plant(models.Model):
    name = models.CharField(max_length=210)
    other_names = models.TextField(default="")
    description = models.TextField(default="")
    species = models.CharField(max_length=200)
    group = models.CharField(max_length=200)
    light = models.TextField(default="")
    irrigation = models.CharField(max_length=200)
    temperature = models.CharField(max_length=200)
    precautions = models.TextField(default="")
    flowering = models.BooleanField(default=False)
    size = models.CharField(max_length=200)
    image_front = models.TextField(default="")
    render = models.TextField(default="")
    created_at = models.DateField(auto_now_add=True)
    inside = models.BooleanField(default=False)