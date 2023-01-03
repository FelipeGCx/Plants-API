from rest_framework import serializers
from plants.models.orderSale import OrderSale

class OrderSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSale
        fields = ["id", "id_products", "address", "payment_method", "payment_state", "order_at"]
        