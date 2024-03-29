"""
Form modules for checkout app
"""
# Imports

# -----------------------------------------------------------------
# 3rd Party
from django import forms

# internal
from .models import Order
# ------------------------------------------------------------------


class OrderForm(forms.ModelForm):
    """
    Create a form for checkout the product by
    using Order model fields
    """
    class Meta:
        model = Order
        fields = ['full_name',  'email', 'phone_number',
                  'country', 'postcode', 'town_or_city', 'street_address1',
                  'street_address2', 'county']

    def __init__(self, *args, **kwargs):
        """
        override default __init__() method to provide
        placeholder, remove labels and set auto focus
        on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County'
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'strype-style-input, rounded-0'
            self.fields[field].label = False
