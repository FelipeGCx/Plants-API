from rest_framework import serializers
from plants.models.poToOs import ProductOrderToOrderSale

class ProductOrderToOrderSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrderToOrderSale
        fields = ["id", "id_product_order", "id_order_sale"]