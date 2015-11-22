from django.db import models
from django_extensions.db.fields import CreationDateTimeField
from model_utils import *
# Create your models here.

# User Model
# Attributes: userId, address, userName, password, email, is_staff
class User(models.Model):
    user_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=150)
    STAFF_CHOICES = (
     ('Y', 'Yes'),
     ('N', 'No'),
    )
    is_staff = models.CharField(max_length=1, choices=STAFF_CHOICES)
    class Meta:
        ordering = ['user_name']

# Order Model
# Attributes: orderId, orderDate, paid
class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='orders')
    product = models.ForeignKey('Product', related_name='orders')
    quantity = models.PositiveSmallIntegerField()
    PAID_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    paid = models.CharField(max_length=1, choices=PAID_CHOICES)
    class Meta:
        ordering = ['-order_date']

# Product Model
# Attributes: productId, productName, price, stock quantity, description, active
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    supplier = models.ManyToManyField('Supplier', related_name="products")
    stock_quantity = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200)
    ACTIVE_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    active = models.CharField(max_length=1, choices=ACTIVE_CHOICES)

# Supplier Model
# Attributes: supplierId, supplierName
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    class Meta:
        ordering = ['supplier_name']
