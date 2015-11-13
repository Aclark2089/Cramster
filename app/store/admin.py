from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(User)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(UserOrder)
admin.site.register(ProductSupplier)
admin.site.register(OrderContent)
