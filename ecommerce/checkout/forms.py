from django import forms
from ..shopping_cart.models import ShippingAddress

class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields='__all__'
        help_texts = {
            "address": "Address...", 
            "state": "State...", 
            "zip": "Zip code..."
        }
        