from django.shortcuts import get_object_or_404, render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.context_processors import csrf
from django.db.models import Q
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'store/base.html')

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
	return render(request, 'store/login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get(***REMOVED***, '')
	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/accounts/invalid/')

def invalid_login(request):
	c = {}
	c.update(csrf(request))
	return render(request, 'store/login.html', {'invalid': True})

def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')

def register_user(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		address = StoreUserForm(request.POST)
		username = request.POST.get('username', '')

		if form.is_valid() * user.is_valid():
			form.save()

			u = User.objects.get(username=username)

			temp = StoreUser(auth_user=u)

			user = StoreUserForm(request.POST, instance=temp)

			user.save()
			return HttpResponseRedirect('/accounts/register_success/')

	args = {}
	args.update(csrf(request))

	args['form'] = UserForm()
	args['user_info'] = StoreUserForm()

	return render(request, 'store/register.html', args)

def register_success(request):
	return render(request, 'store/register_success.html')

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

	return render(request, 'store/settings.html', args)

def delete_user(request, user_id):
	try:
		user_id = int(user_id)
	except ValueError:
		raise Http404()

	auth.logout(request)
	user_to_delete = User.objects.get(pk=user_id)
	user_to_delete.delete()
	return render(request, 'store/base.html')

def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'store/product_catalog.html', { "products": products })

def edit_product(request, product_id="1"):
	try:
		product_id = int(product_id)
	except ValueError:
		raise Http404()

	if request.method == 'POST':

		current_product = Product.objects.get(pk=product_id)
		form = ProductForm(request.POST, instance=current_product)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/products/')

	product = get_object_or_404(Product, pk=product_id)

	args = {}
	args.update(csrf(request))

	args['form'] = ProductForm(instance=product)
	args['product'] = product
	return render('store/product_edit.html', args)

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'store/supplier_list.html', { "suppliers": suppliers })

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
