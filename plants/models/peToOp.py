from django.db import models
from plants.models.orderPurchase import OrderPurchase
from plants.models.productEntry import ProductEntry
# Create your models here.

class ProductEntryToOrderPurchase(models.Model):
    id_product_entry = models.ForeignKey(ProductEntry, on_delete=models.CASCADE, default="")
    id_order_purchase = models.ForeignKey(OrderPurchase, on_delete=models.CASCADE, default="")
    