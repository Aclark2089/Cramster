from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = format_suffix_patterns([
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

    url(r'^products/$', views.product_catalog, name='product_catalog'),
    url(r'^products/edit/([0-9]+)/$', views.edit_product, name='edit_product'),
    url(r'^suppliers/', views.supplier_list, name='supplier_list'),
    url(r'^accounts/$', views.user_list, name='user_list'),

    # Login urls
    url(r'^accounts/login/', views.login, name='login'),
    url(r'^accounts/auth/', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/', views.logout, name='logout'),
    url(r'^accounts/invalid/', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/', views.register_user, name='register_user'),
    url(r'^accounts/register_success/', views.register_success, name='register_success'),

    url(r'^accounts/settings/', views.settings, name='settings'),
    url(r'^accounts/delete/([0-9]+)/$', views.delete_user, name='delete_user'),
])
