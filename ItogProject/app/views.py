from django.shortcuts import render
from .models import ProductCategory, Product, Customer, Order, OrderDetail, Supplier, Shipment, Employee


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