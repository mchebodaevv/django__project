from django.shortcuts import render
from .models import ProductCategory

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def tovar(request):
    return render(request, 'app/tovar.html')

def category(request):
    categories = ProductCategory.objects.all()
    return render(request, 'app/category.html', {'categories': categories})
