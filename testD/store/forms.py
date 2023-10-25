from django import forms


class ProductForm (forms.Form):
    name = forms.CharField(max_length=256, required=True)
    price = forms.FloatField(min_value=0)