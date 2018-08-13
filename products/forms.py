from django import forms

from .models import Products


class ProductForm(forms.ModelForm):
    name = forms.CharField(required=True,
                            widget=forms.TextInput(
                                attrs={
                                    "type": "text",
                                    "class": "form-control",
                                    "placeholder": "Product name"
                                }))
    class Meta:
        model = Products
        fields = ['name']