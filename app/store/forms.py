from django.forms import ModelForm
from .models import *

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['address', 'email', 'is_staff']
		labels = {
			'is_staff': ('Check this if you are a staff member'),
		}
