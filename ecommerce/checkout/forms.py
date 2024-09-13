from django import forms
from shopping_cart.models import ShippingAddress

class ShippingInfoForm(forms.ModelForm):
    class Meta:
        model=ShippingAddress
        fields='__all__'

    def __init__(self, *args, **kwargs): 
        super(ShippingInfoForm, self).__init__(*args, **kwargs)

        self.fields['address'].widget.attrs['placeholder'] = 'Address...'
        self.fields['state'].widget.attrs['placeholder'] = 'State...'
        self.fields['zip'].widget.attrs['placeholder'] = 'Zip code...'