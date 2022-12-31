from rest_framework import serializers
from plants.models.orderPurchase import OrderPurchase

class OrderPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPurchase
        fields = ["id", "id_products", "total_cost", "order_at"]
        
    def tp_representatio(self, obj):
        order = OrderPurchase.objects.get(id=obj.id)
        return {
            "id": order.id, 
            "id_products": order.id_products, 
            "total_cost": order.total_cost, 
            "order_at": order.order_at
        }