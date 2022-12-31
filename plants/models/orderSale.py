from django.db import models
# from plants.models.poToOs import ProductOrderToOrderSale
# Create your models here.

class OrderSale(models.Model):
    id_products = models.IntegerField()
    # id_products = models.ForeignKey(ProductOrderToOrderSale, on_delete=models.CASCADE, default="")
    address = models.TextField()
    payment_method = models.TextField()
    payment_state = models.BooleanField()
    order_at = models.DateField(auto_now_add=True)