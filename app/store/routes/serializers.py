from rest_framework import serializers
from store.models import *

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'user_name', 'orders', 'email', 'is_staff')

class ProductSerializer(serializers.ModelSerializer):
    supplies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    product_order_number = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'supplies', 'stock_quantity', 'description', 'active')

class OrderSerializer(serializers.ModelSerializer):
    contains = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('order_date', 'user', 'order_manifest', 'paid')


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'products')

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ['order', 'product', 'quantity']
