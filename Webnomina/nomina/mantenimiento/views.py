from django.shortcuts import render,HttpResponse

from mantenimiento.models import Cargo
from .forms import  CargoForm
from .models import Cargo


# Create your views here.
def inicio(request):
    #return HttpResponse("<h1>Bienvenidos a mi Sitio Web</h1>")
    return render(request, "inicio.html")

# vistas de Cargos
def crearCargo(request):
    print(request)
    print(request.method)
    if request.method == "POST":
        print("entro por post")
        cargo_form = CargoForm(request.POST)
        if cargo_form.is_valid():
            cargo_form.save()
    else:
        print("entro por get")
        cargo_form = CargoForm()
    cargos = Cargo.objects.all()
    return render(request,"pages/cargo.html",{'cargoForm':cargo_form, 'cargos':cargos, 'accion':'Crear'})
def editarCargo(request,cod):
    error,cargo_form=None,None
    try:
        cargo = Cargo.objects.get(id=cod) 
        if request.method == "GET":
            cargo_form = CargoForm(instance=cargo)
    except Exception as e:
        error=e
    
    






# vistas de departamentos






# vistas de empleados



# def cargo(request):
#     #return HttpResponse("<h1>Mantenimiento de Cargos</h1>")
#     return render(request,"pages/cargo.html")


def departamento(request):
    #return HttpResponse("<h1>Mantenimiento de Departamentos</h1>")
    return render(request,"pages/departamento.html")

def empleado(request):
    #return HttpResponse("<h1>Mantenimiento de Empleados</h1>")
    return render(request,"pages/empleado.html")
