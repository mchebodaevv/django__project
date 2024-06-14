from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('tovar',views.tovar, name='tovar'),
    path('category', views.category,name = 'category'),
 ]
