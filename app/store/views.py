from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def form(request):
    return HttpResponse("The form would normally be here")
