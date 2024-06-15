from .models import ProductCategory
from django import forms
from django.forms import ModelForm,TextInput

class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name']
        widgets = {
            'category_name': TextInput(attrs={
                'placeholder': 'Название категории'
            })
        }
