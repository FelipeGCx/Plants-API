from rest_framework import serializers
from plants.models.poToOs import ProductOrderToOrderSale

class ProductOrderToOrderSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderToOrderSale
        fields = ["id", "id_product_order", "id_order_sale"]
        
    def tp_representatio(self, obj):
        orden = ProductOrderToOrderSale.objects.get(id=obj.id)
        return {
            "id": orden.id, 
            "id_product_order": orden.id_product_order, 
            "id_order_sale": orden.id_order_sale, 
        }