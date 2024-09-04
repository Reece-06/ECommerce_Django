from django.shortcuts import render
from .models import *
# Create your views here.

def AllProducts(request):
    all_products = Product.objects.all()
    return render(request, "shopping_cart/all-products.html", {
        "products": all_products,
    })

def Cart(request):
    return render(request, "shopping_cart/cart.html")