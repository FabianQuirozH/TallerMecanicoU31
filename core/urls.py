from django.urls import path
from .views import *
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', index, name="index" ),
    path('vehiculos', vehiculos, name="vehiculos" ),
    path('about', about, name="about" ),
    path('mecanicos', mecanicos, name="mecanicos" ),
    path('contact', contact, name="contact" ),
    path('services', services, name="services" ),
    path('listarmecanicos/', listarmecanicos, name="listarmecanicos" ),
    path('listarproductos/', listarproductos, name="listarproductos" ),
    path('administrador', administrador, name="administrador" ),
    path('empleadosadd', empleadosadd, name="empleadosadd" ),
    path('producto_create', producto_create, name="producto_create" ),
    path('producto/<int:producto_id>', producto_show, name="producto_show" ),
    path('empleadosupdate/<int:id>/', empleadosupdate, name='empleadosupdate'),
    path('empleadosdelete/<int:id>/', empleadosdelete, name='empleadosdelete'),
    path('producto_edit/<int:id>/', producto_edit, name='producto_edit'),
    path('producto_delete/<int:id>/', producto_delete, name='producto_delete'),
    path('account_locked/', account_locked, name="account_locked" ),
    path('registro', registro, name="registro" ),
    path('carrito/',carrito, name="carrito"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    

     # CARRITO
    path('carrito', carrito_index, name="carrito_index"),
    path('carrito/agregar', carrito_save, name="carrito_save"),
    path('carrito/clean', carrito_clean, name="carrito_clean"),
    path('item_carrito/<int:item_carrito_id>/eliminar', item_carrito_delete, name="item_carrito_delete"),
]


