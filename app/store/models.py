from django.db import models

# Create your models here.

# User Model
# Attributes: userId, address, userName, password, email, is_staff
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    STAFF_CHOICES = (
     ('Y', 'Yes'),
     ('N', 'No'),
    )
    is_staff = models.CharField(max_length=1, choices=STAFF_CHOICES)


# Order Model
# Attributes: orderId, orderDate, paid
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_date = models.DateField()
    PAID_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    paid = models.CharField(max_length=1, choices=PAID_CHOICES)

# Product Model
# Attributes: productId, productName, price, stock quantity, description, active
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.DateField()
    price = models.IntegerField()
    stock_quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    ACTIVE_CHOICES = (
    ('Y', 'Yes'),
    ('N', 'No'),
    )
    active = models.CharField(max_length=1, choices=ACTIVE_CHOICES)

# Supplier Model
# Attributes: supplierId, supplierName
class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=50)

# userOrder Model
# Attributes: user, order
class UserOrder(models.Model):
    user = models.ForeignKey(User)
    order = models.ManyToManyField(Order)

# orderContent Model
# Attributes: order, product, quantity
class OrderContent(models.Model):
    order = models.ManyToManyField(Order)
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField()

# productSupplied Model
# Attributes: product, supplier
class ProductSupplier(models.Model):
    product = models.ManyToManyField(Product)
    supplier = models.ManyToManyField(Supplier)
