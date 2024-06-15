from .models import ProductCategory, Product, Customer, Order, Supplier, Shipment, Employee
from django import forms
from django.forms import ModelForm, TextInput, IntegerField, NumberInput, Textarea, DateInput


class ProductCategoryForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = ['category_name']
        widgets = {
            'category_name': TextInput(attrs={
                'placeholder': 'Название категории'
            })
        }


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'quantity', 'category']
        category = forms.ModelChoiceField(
            queryset=ProductCategory.objects.all(),
            empty_label="Выберите категорию",
            widget=forms.Select(attrs={'class': 'select'})
        )
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Название товара'
            }),
            'description': Textarea(attrs={
                'placeholder': 'Описание товара'
            }),
            'quantity': NumberInput(attrs={
                'placeholder': 'Количество товара'
            }),

        }


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': TextInput(attrs={
                'placeholder': 'Имя клиента'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Электронная почта'
            }),
            'phone': TextInput(attrs={
                'placeholder': 'Телефон'
            }),
            'address': TextInput(attrs={
                'placeholder': 'Адрес'
            }),

        }


class ZakazForm(forms.ModelForm):
    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(),
        empty_label="Выберите клиента",
        widget=forms.Select(attrs={'class': 'select'})
    )
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label="Выберите продукт",
        widget=forms.Select(attrs={'class': 'select'})
    )
    class Meta:
        model = Order
        fields = ['order_date', 'customer', 'product', 'quantity']
        widgets = {
            'order_date': forms.DateInput(attrs={'placeholder': 'Дата заказа'}),
        }
class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'contact_info', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя поставщика'}),
            'contact_info': forms.TextInput(attrs={'placeholder': 'Контакты'}),
            'address': forms.TextInput(attrs={'placeholder': 'Адрес'}),
        }
class ShipmentForm(forms.ModelForm):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(),
        empty_label="Выберите продукт",
        widget=forms.Select(attrs={'class': 'select'})
    )
    supplier = forms.ModelChoiceField(
        queryset=Supplier.objects.all(),
        empty_label="Выберите поставщика",
        widget=forms.Select(attrs={'class': 'select'})
    )
    class Meta:
        model = Shipment
        fields = ['supplier', 'product', 'shipment_date', 'quantity']
        widgets = {
            'supplier': forms.TextInput(attrs={'placeholder': 'Имя поставщика'}),
            'shipment_date': forms.TextInput(attrs={'placeholder': 'Дата поставки'}),
            'quantity': forms.NumberInput(attrs={'placeholder': 'Количество'}),
        }
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'position']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя поставщика'}),
            'email': forms.TextInput(attrs={'placeholder': 'Электронная почта'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон'}),
            'position': forms.TextInput(attrs={'placeholder': 'Должность'}),
        }