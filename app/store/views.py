from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from rest_framework import viewsets
# Create your views here.

def index(request):
    return render(request, 'store/base.html')

def form(request):
    return HttpResponse("The form would normally be here")
