from django.shortcuts import render, redirect
from .models import ProductCategory, Product, Customer, Order, OrderDetail, Supplier, Shipment, Employee
from .forms import ProductCategoryForm
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


def zakaz_detail(request):
    zakaz_details = OrderDetail.objects.all()
    return render(request, 'app/zakaz_detail.html', {'zakaz_details': zakaz_details})


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
