from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="index"),
    path("crearUser/", views.crearUser, name="crearUser" ),
    path("signout/", views.signout, name="signout"),
    path("signin/", views.signin, name="signin"),
    path("info/", views.info, name="info"),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'),
    path("mostrar_productos/", views.mostrar_productos, name="mostrar_productos"),
    path("mostrar_materiales/", views.mostrar_materiales, name="mostrar_materiales"),
    path("crear_materiales_unitarios", views.crear_materiales_unitarios, name="crear_materiales_unitarios"),
    path("crear_materiales_gramos", views.crear_materiales_gramos, name="crear_materiales_gramos"),
]