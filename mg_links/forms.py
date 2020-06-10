from django import forms
from .models import Product

class AddProduct(forms.Form):
    product_name = forms.CharField(max_length=200, label='Product')
    key_word = forms.CharField(max_length=200, label='Key_word ', widget=forms.TextInput(attrs={'placeholder': 'Future search term'}))
    link = forms.CharField(max_length=500, label='Link') 

    class Meta:
        model = Product 


class SearchProduct(forms.Form):
    looking_for = forms.CharField(max_length=200, label='Key_word search')

