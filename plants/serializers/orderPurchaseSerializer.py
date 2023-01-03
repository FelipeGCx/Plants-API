from rest_framework import serializers
from plants.models.orderPurchase import OrderPurchase

class OrderPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPurchase
        fields = ["id", "id_products", "total_cost", "order_at"]
        