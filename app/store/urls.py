from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = format_suffix_patterns([

    # Index URLs
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^oversell/$', views.oversell, name='oversell'),

    # Products URLs
    url(r'^products/$', views.product_catalog, name='product_catalog'),
    url(r'^products/add/$', views.add_product, name='add_product'),
    url(r'^products/([0-9]+)/$', views.product_catalog, name='product_filter'),
    url(r'^products/edit/([0-9]+)/$', views.edit_product, name='edit_product'),
    url(r'^products/delete/([0-9]+)/$', views.delete_product, name='delete_product'),

    # Orders URLs
    url(r'^orders/$', views.orders, name='orders'),
    url(r'^orders/open/$', views.open_orders, name='open_orders'),
    url(r'^orders/more/([0-9]+)/$', views.orders_more, name='orders_more'),
    url(r'^orders/checkout/([0-9]+)/$', views.orders_checkout, name='orders_checkout'),
    url(r'^orders/list/$', views.order_list, name='orders_list'),
    url(r'^orders/edit/([0-9]+)/$', views.order_edit, name='order_edit'),

    # Suppliers URLs
    url(r'^suppliers/$', views.supplier_list, name='supplier_list'),


    # Accounts URLs
    url(r'^accounts/$', views.user_list, name='user_list'),
    url(r'^accounts/edit/([0-9]+)/$', views.user_edit, name='user_edit'),
    url(r'^accounts/new/$', views.user_new, name='user_new'),
    url(r'^accounts/settings/$', views.settings, name='settings'),
    url(r'^accounts/delete/([0-9]+)/$', views.delete_user, name='delete_user'),

    # Login urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),

])
