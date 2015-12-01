from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404
from django.db.models import Q
from .models import *
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

def search(request):
	if 'q' in request.GET and request.GET['q']:
		q = request.GET['q']
		products = Product.objects.all().filter(Q(product_name__icontains=q) | Q(description__icontains=q))
		result = {
			'products': products,
			'query': q,
		}
		return render(request, 'store/search_results.html', result)

	else:
		 message = 'You submitted an empty form.'
	return HttpResponse(message)
