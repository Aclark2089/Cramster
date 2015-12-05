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


def search(request, filter=None):
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

		if form.is_valid() * address.is_valid():
			form.save()

			u = User.objects.get(username=username)

			temp = StoreUser(auth_user=u)

			user = StoreUserForm(request.POST, instance=temp)

			user.save()
			return render(request, 'store/login.html')

	args = {}
	args.update(csrf(request))

	args['form'] = UserForm()
	args['user_info'] = StoreUserForm()

	return render(request, 'store/register.html', args)

def settings(request):
	current_user = User.objects.get(username=request.user.username)
	error = False

	if request.method == 'POST':

		form1 = UserForm(request.POST, instance=current_user)
		form2 = StoreUserForm(request.POST, instance=current_user.storeuser)

		if form1.is_valid() * form2.is_valid():
			form1.save()
			form2.save()
			return HttpResponseRedirect('/accounts/login/')

		error = True


	args = {}
	args.update(csrf(request))

	if error:
		args['error'] = True
	args['form1'] = UserForm(instance=current_user)
	args['form2'] = StoreUserForm(instance=current_user.storeuser)
	args['current_user'] = current_user
	return render(request, 'store/settings.html', args)

def delete_user(request, user_id):
	try:
		user_id = int(user_id)
	except ValueError:
		raise Http404()

	if user_id == request.user.id:
		auth.logout(request)

	user_to_delete = User.objects.get(pk=user_id)
	storeuser_to_delete = user_to_delete.storeuser

	user_to_delete.delete()
	storeuser_to_delete.delete()

	return render(request, 'store/base.html')

def product_catalog(request, filter=None):
    if filter == 1:
        products = Product.objects.all().order_by('price')
    elif filter == 2:
        products = Product.objects.all().order_by('product_name')
    else:
        products = Product.objects.all()
    return render(request, 'store/product_catalog.html', { "products": products })

def add_product(request):
	if request.method == 'POST':

		form = NewProductForm(request.POST)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/products/')

	args = {}
	args.update(csrf(request))

	args['form'] = NewProductForm()
	return render(request, 'store/product_add.html', args)

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
	return render(request, 'store/product_edit.html', args)

def delete_product(request, product_id):
	try:
		product_id = int(product_id)
	except ValueError:
		raise Http404()

	if request.method == 'POST':
		product = get_object_or_404(Product, pk=product_id)
		product.delete()
		return HttpResponseRedirect('/products/')

def orders(request):

	if request.method == 'POST':

		order = Order(user=user.storeuser, paid=False)
		form = ProductForm(request.POST, instance=order)

		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/orders/pay/')


	args = {}
	args.update(csrf(request))

	args['form'] = OrderForm()
	return render(request, 'store/product_edit.html', args)
	return render(request, 'store/orders.html')

def orders_pay(request):
	return render(request, 'store/orders_pay.html')

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'store/supplier_list.html', { "suppliers": suppliers })

def user_list(request):
	users = User.objects.all()
	return render(request, 'store/user_list.html', { "users": users })

def user_edit(request, user_id):
    try:
        user_id = int(user_id)
    except ValueError:
        raise Http404()

    if request.method == 'POST':
        auth_user = User.objects.get(id=user_id)
        form1 = UserForm(request.POST, instance=auth_user)
        form2 = StoreUserForm(request.POST, instance=auth_user.storeuser)
        if form1.is_valid() * form2.is_valid():
            form1.save()
            form2.save()
            return HttpResponseRedirect('/accounts/')

    current_user = get_object_or_404(User, id=user_id)
    args = {}
    args.update(csrf(request))
    args['form1'] = UserForm(instance=current_user)
    args['form2'] = StoreUserForm(instance=current_user.storeuser)
    args['user_id'] = user_id

    return render(request, 'store/user_edit.html', args)

def user_new(request):
	args = {}
	args.update(csrf(request))

	args['form'] = UserForm()
	args['user_info'] = StoreUserForm()
	args['new'] = True

	return render(request, 'store/register.html', args)
