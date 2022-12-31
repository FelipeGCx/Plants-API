from django.db import models
# from plants.models.peToOp import ProductEntryToOrderPurchase
# Create your models here.

class OrderPurchase(models.Model):
    id_products = models.IntegerField()
    total_cost = models.BigIntegerField()
    order_at = models.DateField(auto_now_add=True)