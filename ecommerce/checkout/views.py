from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .forms import ShippingInfoForm
# Create your views here.

class CheckoutView(View):
    def get(self, request):
        form = ShippingInfoForm()
        
        return render("request", "/checkout/checkout.html", {
            "form": form, 

        })

    def post(self, request):
        form = ShippingInfoForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponseRedirect(reverse("all-products"))

        return render("request", "/checkout/checkout.html", {
            "form": form,
        }) 