from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .models import *

urlpatterns = format_suffix_patterns([
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),

    # Login urls
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/auth/$', views.auth_view, name='auth_view'),
    url(r'^accounts/logout/$', views.logout, name='logout'),
    url(r'^accounts/loggedin/$', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid/$', views.invalid_login, name='invalid_login'),
    url(r'^accounts/register/$', views.register_user, name='register_user'),
    url(r'^accounts/register_success/$', views.register_success, name='register_success'),
])
