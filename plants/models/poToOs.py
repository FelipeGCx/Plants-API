from django.db import models
from plants.models.orderSale import OrderSale
from plants.models.productOrder import ProductOrder
# Create your models here.

class ProductOrderToOrderSale(models.Model):
    id_product_order = models.ForeignKey(ProductOrder, on_delete=models.CASCADE, default="")
    id_order_sale = models.ForeignKey(OrderSale, on_delete=models.CASCADE, default="")
    