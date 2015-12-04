from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class UserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	address = forms.TextField(required=True)

	class Meta:
		model = User
		fields = {'username', 'email', 'address', 'password1', 'password2'}

	def save(self, commit=True):
		user = super(UserCreationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.address = self.cleaned_data['address']

		if commit:
			user.save()

		return user

class ProductForm(ModelForm):
	class Meta:
		model = Product
		fields = {'product_name', 'price', 'supplier', 'stock_quantity', 'description', 'active'}
	