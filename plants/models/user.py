from django.db import models
# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=210)
    password = models.CharField(max_length=210)
    roles = models.TextField(default="USER_ROLE")