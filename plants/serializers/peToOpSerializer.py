from rest_framework import serializers
from plants.models.peToOp import ProductEntryToOrderPurchase

class ProductEntryToOrderPurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductEntryToOrderPurchase
        fields = ["id", "id_product_entry", "id_order_purchase"]
