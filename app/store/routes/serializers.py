from rest_framework import serializers
from django.contrib.auth.models import User
from store.models import *

class AuthUserSerializer(serializers.ModelSerializer):
    storeuser = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = User
        fields = ('__all__')

class StoreUserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = StoreUser
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'supplier', 'orders', 'stock_quantity', 'description', 'active')

class OrderSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Order
        fields = ('order_date', 'user', 'products', 'paid')


class SupplierSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'products')

class ProductOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOrder
        fields = ('product', 'order', 'quantity')
