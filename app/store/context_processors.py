from .models import Product

def store(request):
    galleryproducts = Product.objects.all()[:3]
    context = {
        "store_title": "Cramster",
        "galleryproducts": galleryproducts
    }
    return context
