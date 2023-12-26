from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ProductoForm, RelacionProductoMaterialGramosForm, RelacionProductoMaterialUnitarioForm, Material_gramos, Material_unitario
from .models import MaterialGramos, MaterialUnitario, Producto

# Create your views here.
def home(request):
    return render(request, "index.html")

# Usuarios
def crearUser(request):
    if request.method == "GET":
        return render(request, "crearUser.html")
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect(home)
            except IntegrityError:
                return render(request, "crearUser.html",{"error":"El usuario ya existe"})

def signout(request):
    logout(request)
    return redirect(home)

def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {"error": "El usuario o contraseña no coinciden"})
        else:
            login(request, user)
            return redirect(home)

def info(request):
    return render(request, "info.html")

# Productos
def agregar_producto(request):
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST)
        relacion_formset_gramos = RelacionProductoMaterialGramosForm(request.POST, prefix='relacion_gramos')
        relacion_formset_unitarios = RelacionProductoMaterialUnitarioForm(request.POST, prefix='relacion_unitarios')

        if producto_form.is_valid() and relacion_formset_gramos.is_valid() and relacion_formset_unitarios.is_valid():
            producto = producto_form.save()
            relacion_gramos = relacion_formset_gramos.save(commit=False)
            relacion_unitarios = relacion_formset_unitarios.save(commit=False)

            for relacion in relacion_gramos:
                relacion.producto = producto
                relacion.save()

            for relacion in relacion_unitarios:
                relacion.producto = producto
                relacion.save()

            return redirect('lista_productos')

    else:
        producto_form = ProductoForm()
        relacion_formset_gramos = RelacionProductoMaterialGramosForm(prefix='relacion_gramos')
        relacion_formset_unitarios = RelacionProductoMaterialUnitarioForm(prefix='relacion_unitarios')

    return render(request, 'agregar_producto.html', {
        'producto_form': producto_form,
        'relacion_formset_gramos': relacion_formset_gramos,
        'relacion_formset_unitarios': relacion_formset_unitarios,
    })

def mostrar_productos(request):
    producto = Producto.objects.all()
    return render(request, "mostrar_productos.html", {
        "producto":producto
    })

# Materiales
def mostrar_materiales(request):
    materialesU = MaterialUnitario.objects.all()
    materialesG = MaterialGramos.objects.all()

    return render(request, "mostrar_materiales.html", {
        "materialesU": materialesU, "materialesG": materialesG
    })

def crear_materiales_gramos(request):
    if request.method == "GET":
        return render(request, "crear_materiales_gramos.html", {
            "form_g": Material_gramos()
        })
    else:
        try:
            # Materiales en Gramos
            form_g = Material_gramos(request.POST)
            if form_g.is_valid():
                form_g.save()
                return redirect("mostrar_materiales")
            else:
                # Si el formulario no es válido, puedes mostrarlo de nuevo con los errores.
                return render(request, "crear_materiales_gramos.html", {"form_g": form_g})
        except ValueError as e:
            return render(request, "crear_materiales_gramos.html", {"error": str(e)})

def crear_materiales_unitarios(request):
    if request.method == "GET":
        return render(request, "crear_materiales_unitarios.html",{
            "form_u": Material_unitario()
        })
    else:
        try:
            form_u = Material_unitario(request.POST)
            form_u.save()
            return redirect("mostrar_materiales")
        except ValueError as e:
            return render(request, "crear_materiales_unitarios.html", {"error": str(e)})

