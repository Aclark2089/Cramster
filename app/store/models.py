from django.db import models
from django.contrib.auth.models import User
from django_extensions.db.fields import CreationDateTimeField
from model_utils import *
# Create your models here.

# User Model
# Attributes: userId, address, userName, password, email, is_staff
class StoreUser(models.Model):
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

# Order Model
# Attributes: orderId, orderDate, paid
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(StoreUser, related_name='orders')
    paid = models.BooleanField()
    class Meta:
        ordering = ['-order_date']

# Product Model
# Attributes: productId, productName, price, stock quantity, description, active
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    supplier = models.ManyToManyField('Supplier', related_name='products')
    stock_quantity = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200)
    active = models.BooleanField()
    class Meta:
        ordering = ['price']

# Supplier Model
# Attributes: supplierId, supplierName
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    class Meta:
        ordering = ['supplier_name']

class ProductOrder(models.Model)
    product = models.ForeignKey('Product', related_name='productorder')
    order = models.ForeignKey('Order', related_name='productorder')
    quantity = models.PositiveSmallIntegerField()