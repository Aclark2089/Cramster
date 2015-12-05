from store.routes.serializers import *
from store.models import *
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, generics, filters
from rest_framework.renderers import TemplateHTMLRenderer

# Auth User
class AuthUserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuthUserSerializer

# Regular User
class StoreUserViewSet(viewsets.ModelViewSet):
    queryset = StoreUser.objects.all()
    serializer_class = StoreUserSerializer

# Product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# Supplier
class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

# Product Order
class ProductOrderViewSet(viewsets.ModelViewSet):
    queryset = ProductOrder.objects.all()
    serializer_class = ProductOrderSerializer
