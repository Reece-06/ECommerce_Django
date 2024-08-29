from django.shortcuts import render

# Create your views here.

def AllProducts(request):
    return render(request, "shopping_cart/all-products.html")