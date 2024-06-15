from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('tovar',views.tovar, name='tovar'),
    path('category', views.category,name = 'category'),
    path('client', views.client,name ='client'),
    path('zakazi', views.zakaz,name ='zakazi'),
    path('zakaz_detail', views.zakaz_detail,name ='zakaz_detail'),
    path('suppliers', views.suppliers,name ='suppliers'),
    path('postavki', views.postavki,name ='postavki'),
    path('sotrudniki', views.sotrudnik,name ='sotrudniki'),
    path('category_create', views.category_create,name ='category_create'),
    path('<int:pk>/category_edit', views.category_edit.as_view(),name = 'category_edit'),
    path('<int:pk>/category_delete', views.category_delete.as_view(),name = 'category_delete'),
 ]
