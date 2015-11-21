from rest_framework import serializers
from store.models import *

class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password = serializers.CharField(style={'input_type': ***REMOVED***})
    class Meta:
        model = User
        fields = ('user_name', 'email', ***REMOVED***, 'orders', 'is_staff')

class ProductSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ('product_name', 'price', 'supplier', 'orders', 'stock_quantity', 'description', 'active')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('order_date', 'user', 'product', 'quantity', 'paid')


class SupplierSerializer(serializers.ModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Supplier
        fields = ('supplier_name', 'products')
