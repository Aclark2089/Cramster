from django.forms import ModelForm
from store.models import *

# User forms
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_name', 'address', ***REMOVED***, 'email', 'is_staff']

# User forms
class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_order', 'price', 'stock_quantity', 'description', 'active']

# User forms
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['order_date', 'user', 'paid']

# User forms
class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplier_name', 'product']
