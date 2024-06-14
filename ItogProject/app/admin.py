from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product, Customer, Order, OrderDetail, Supplier, Shipment, Employee

admin.site.register(ProductCategory)
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Supplier)
admin.site.register(Shipment)
admin.site.register(Employee)

