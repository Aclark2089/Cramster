from .models import Product

def store(request):
    galleryproducts = Product.objects.all()[:3]
    cart = {}
    context = {
        "store_title": "Cramster",
        "galleryproducts": galleryproducts,
        "cart": {},
    }
    return context
