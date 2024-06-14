from django.contrib import admin

# Register your models here.
from .models import ProductCategory

admin.site.register(ProductCategory)