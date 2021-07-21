from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_firstname', 'customer_lastname','address', 'telephone','email']