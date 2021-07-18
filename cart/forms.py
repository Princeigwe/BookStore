from django import forms

class QuantityForm(forms.Form):
    quantity = forms.IntegerField(max_value=20, min_value=1)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
