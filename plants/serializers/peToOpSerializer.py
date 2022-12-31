from rest_framework import serializers
from plants.models.peToOp import ProductEntryToOrderPurchase

class ProductEntryToOrderPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntryToOrderPurchase
        fields = ["id", "id_product_entry", "id_order_purchase"]
        
    def tp_representatio(self, obj):
        orden = ProductEntryToOrderPurchase.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "id_product_entry": orden.id_product_entry, 
            "id_order_purchase": orden.id_order_purchase, 
        }