from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/', views.form, name='form'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
