from rest_framework import serializers
from plants.models.orderSale import OrderSale

class OrderSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSale
        fields = ["id", "id_products", "address", "payment_method", "payment_state", "order_at"]
        
    def tp_representatio(self, obj):
        orden = OrderSale.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "id_products": orden.id_products, 
            "address": orden.address, 
            "payment_method": orden.payment_method,
            "payment_state": orden.payment_state,
            "order_at": orden.order_at
        }