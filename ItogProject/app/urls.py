from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('tovar',views.tovar, name='tovar'),
    path('category', views.category,name = 'category'),
    path('client', views.client,name ='client'),
    path('zakazi', views.zakaz,name ='zakazi'),
    path('suppliers', views.suppliers,name ='suppliers'),
    path('postavki', views.postavki,name ='postavki'),
    path('sotrudniki', views.sotrudnik,name ='sotrudniki'),
    path('category_create', views.category_create,name ='category_create'),
    path('<int:pk>/category_edit', views.category_edit.as_view(),name = 'category_edit'),
    path('<int:pk>/category_delete', views.category_delete.as_view(),name = 'category_delete'),
    path('tovar_create', views.tovar_create,name ='tovar_create'),
    path('<int:pk>/tovar_edit', views.tovar_edit.as_view(),name = 'tovar_edit'),
    path('<int:pk>/tovar_delete', views.tovar_delete.as_view(),name = 'tovar_delete'),
    path('client_create', views.client_create,name ='client_create'),
    path('<int:pk>/client_edit', views.client_edit.as_view(),name = 'client_edit'),
    path('<int:pk>/client_delete', views.client_delete.as_view(),name = 'client_delete'),
    path('zakaz_create', views.zakaz_create,name ='zakaz_create'),
    path('<int:pk>/zakaz_edit', views.zakaz_edit.as_view(),name = 'zakaz_edit'),
    path('<int:pk>/zakaz_delete', views.zakaz_delete.as_view(),name = 'zakaz_delete'),
    path('suppliers_create', views.suppliers_create,name ='suppliers_create'),
    path('<int:pk>/suppliers_edit', views.suppliers_edit.as_view(),name = 'suppliers_edit'),
    path('<int:pk>/suppliers_delete', views.suppliers_delete.as_view(),name = 'suppliers_delete'),
    path('postavki_create', views.postavki_create,name ='postavki_create'),
    path('<int:pk>/postavki_edit', views.postavki_edit.as_view(),name = 'postavki_edit'),
    path('<int:pk>/postavki_delete', views.postavki_delete.as_view(),name = 'postavki_delete'),
    path('sotrudnik_create', views.sotrudnik_create,name ='sotrudnik_create'),
    path('<int:pk>/sotrudnik_edit', views.sotrudnik_edit.as_view(),name = 'sotrudnik_edit'),
    path('<int:pk>/sotrudnik_delete', views.sotrudnik_delete.as_view(),name = 'sotrudnik_delete'),
 ]
