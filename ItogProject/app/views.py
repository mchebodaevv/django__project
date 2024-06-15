from django.shortcuts import render, redirect
from .models import ProductCategory, Product, Customer, Order,  Supplier, Shipment, Employee
from .forms import ProductCategoryForm, ProductForm, CustomerForm, ZakazForm, SuppliersForm, ShipmentForm, EmployeeForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

def index(request):
    return render(request, 'app/index.html')


def tovar(request):
    products = Product.objects.all()
    return render(request, 'app/tovar.html', {'products': products})


def category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'app/category.html', {'categories': categories})


def client(request):
    clients = Customer.objects.all()
    return render(request, 'app/client.html', {'clients': clients})


def zakaz(request):
    zakazi = Order.objects.all()
    return render(request, 'app/zakaz.html', {'zakazi': zakazi})




def suppliers(request):
    suppliers = Supplier.objects.all()
    return render(request, 'app/suppliers.html', {'suppliers': suppliers})


def postavki(request):
    postavki = Shipment.objects.all()
    return render(request, 'app/postavki.html', {'postavki': postavki})


def sotrudnik(request):
    sotrudniki = Employee.objects.all()
    return render(request, 'app/sotrudnik.html', {'sotrudniki': sotrudniki})


def category_create(request):
    error = ''
    if request.method == 'POST':
        form = ProductCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
        else:
            error = 'Данные неверные'
    form = ProductCategoryForm
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'app/category_create.html', data)


class category_edit(UpdateView):
    model = ProductCategory
    template_name = 'app/category_edit.html'
    fields = ['category_name']


class category_delete(DeleteView):
    model = ProductCategory
    template_name = 'app/category_delete.html'
    success_url = '/category'
    fields = ['category_name']

from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import ProductCategory

def tovar_create(request):
    error = ''
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tovar')
        else:
            error = 'Данные неверные'


    form = ProductForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/tovar_create.html', data)
class tovar_edit(UpdateView):
    model = Product
    template_name = 'app/tovar_edit.html'
    fields = ['name','description','quantity','category']
class tovar_delete(DeleteView):
    model = Product
    template_name = 'app/tovar_delete.html'
    success_url = '/tovar'
    fields = ['name']
def client_create(request):
    error = ''
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
        else:
            error = 'Данные неверные'
    form = CustomerForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/client_create.html', data)

class client_edit(UpdateView):
    model = Customer
    template_name = 'app/client_edit.html'
    fields = ['name','email','phone','address']
class client_delete(DeleteView):
    model = Customer
    template_name = 'app/client_delete.html'
    success_url = '/client'
    fields = ['name']


def zakaz_create(request):
    error = ''
    if request.method == 'POST':
        form = ZakazForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)

            # Получаем заказанный товар и уменьшаем его количество
            product = order.product
            if product.quantity >= order.quantity:
                product.quantity -= order.quantity
                product.save()
                order.save()
                return redirect('/zakazi')
            else:
                error = 'Недостаточно товара на складе'
        else:
            error = 'Данные неверные'

    form = ZakazForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/zakaz_create.html', data)


class zakaz_edit(UpdateView):
    model = Order
    template_name = 'app/zakaz_edit.html'
    fields = ['order_date','customer', 'product', 'quantity']
class zakaz_delete(DeleteView):
    model = Order
    template_name = 'app/zakaz_delete.html'
    success_url = '/zakazi'
    fields = ['id']

def suppliers_create(request):
    error = ''
    if request.method == 'POST':
        form = SuppliersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/suppliers')
        else:
            error = 'Данные неверные'
    form = SuppliersForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/suppliers_create.html', data)

class suppliers_edit(UpdateView):
    model = Supplier
    template_name = 'app/suppliers_edit.html'
    fields = ['name','contact_info', 'address']
class suppliers_delete(DeleteView):
    model = Supplier
    template_name = 'app/suppliers_delete.html'
    success_url = '/suppliers'
    fields = ['name']


def postavki_create(request):
    error = ''
    if request.method == 'POST':
        form = ShipmentForm(request.POST)
        if form.is_valid():
            shipment = form.save(commit=False)

            # Получаем поставленный товар и увеличиваем его количество
            product = shipment.product
            product.quantity += shipment.quantity
            product.save()
            shipment.save()
            return redirect('postavki')  # Используем имя URL для редиректа
        else:
            error = 'Данные неверные'

    form = ShipmentForm()
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/postavki_create.html', data)


class postavki_edit(UpdateView):
    model = Shipment
    template_name = 'app/postavki_edit.html'
    fields = ['supplier', 'product', 'shipment_date', 'quantity']
class postavki_delete(DeleteView):
    model = Shipment
    template_name = 'app/postavki_delete.html'
    success_url = '/postavki'
    fields = ['id']
def sotrudnik_create(request):
    error = ''
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/sotrudniki')
        else:
            error = 'Данные неверные'
    form = EmployeeForm
    data = {
        'form': form,
        'error': error,
    }
    return render(request, 'app/sotrudnik_create.html', data)
class sotrudnik_edit(UpdateView):
    model = Employee
    template_name = 'app/sotrudnik_edit.html'
    fields = ['name', 'email', 'phone', 'position']
class sotrudnik_delete(DeleteView):
    model = Employee
    template_name = 'app/sotrudnik_delete.html'
    success_url = '/sotrudniki'
    fields = ['name']