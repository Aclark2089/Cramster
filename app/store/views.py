from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
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
		return render(request, 'store/base.html', {'empty_search': True})

# Login Views
def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('store/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get(***REMOVED***, '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def loggedin(request):
	return render_to_response('store/base.html', {'full_name': request.user.username})

def invalid_login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('store/login.html', {'invalid': True})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def register_user(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)

		username = request.POST.get('username', '')
		password = request.POST.get(***REMOVED***, '')
		login_info = User(username=username, password=password)

		user = UserForm(request.POST, instance=login_info)

		if form.is_valid() * user.is_valid():
			form.save()
			user.save()
			return HttpResponseRedirect('/accounts/register_success/')

	args = {}
	args.update(csrf(request))

	args['form'] = UserCreationForm()
	args['user_info'] = UserForm()

	return render_to_response('store/register.html', args)

def register_success(request):
	return render_to_response('store/register_success.html')

def settings(request):
	if request.method == 'POST':

		current_user = User.objects.get(username=request.user.username)
		form = UserForm(request.POST, instance=current_user)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/settings/')

	args = {}
	args.update(csrf(request))

	args['form'] = UserForm

	return render_to_response('store/settings.html', args)

def delete_user(request, user_id):
	try:
		user_id = int(user_id)
	except ValueError:
		raise Http404()

	auth.logout(request)
	user_to_delete = User.objects.get(pk=user_id)
	user_to_delete.delete()
	return render(request, 'store/base.html')

'''
def staff(request):
	return render(request, 'store/staff.html')

def staff_users(request):
	return render(request, 'store/staff_users.html')

def edit_user(request, user_id):
	try:
		user_id = int(user_id)
	except ValueError:
		raise Http404()

	selected_user = User.objects.get(pk=user_id)
	selected_user.

def staff_products(request):
	return render(request, 'store/staff_products.html')

def staff_orders(request):
	return render(request, 'store/staff_orders.html')

'''