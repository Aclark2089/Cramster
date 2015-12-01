from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = format_suffix_patterns([
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login')
    url(r'^search/', views.search, name='search')
])
