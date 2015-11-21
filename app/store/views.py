from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return render(request, 'store/base.html')

def login(request):
    return render(request, 'store/login.html')
