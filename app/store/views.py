from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
# Create your views here.

def index(request):
    title = "Cramster"
    username = ""
    if request.user.is_authenticated():
        username = (request.user)
    context = {
        "store_title": title,
        "template_username": username,
    }
    return render(request, 'store/base.html', context)

def login(request):
    return render(request, 'store/login.html')
