from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = format_suffix_patterns([
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

    # Login urls
    url(r'^accounts/login/', views.login, name='login'),
    url(r'^accounts/auth/', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/', views.logout, name='logout'),
    url(r'^accounts/invalid/', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/', views.register_user, name='register_user'),
    url(r'^accounts/register_success/', views.register_success, name='register_success'),

    url(r'^accounts/settings/', views.settings, name='settings'),
    url(r'^accounts/delete/(?P<user_id>[0-9]+)/$', views.delete_user, name='delete_user'),

    # Staff Settings
    #url(r'^staff/', views.staff, name='staff'),
    #url(r'^staff/users/', views.staff_users, name='staff_users'),
    #url(r'^staff/users/edit/(?P<user_id>[0-9]+)/$', views.edit_user, name='edit_user'),
    #url(r'^staff/products/', views.staff_products, name='staff_products'),
    #url(r'^staff/orders/', views.staff_orders, name='staff_orders'),
])
