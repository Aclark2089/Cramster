from django.conf.urls import url
from . import views
from .models import *

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^form/', views.form, name='form'),
]
