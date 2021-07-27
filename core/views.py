from django.shortcuts import render, redirect
from . models import animales, nuevoUsuario
from . models import compras
from .forms import CuentaForm, validarUsuario, animalesForm, ComprasForm

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

def ingresar(request):
    return render(request, 'core/ingresar.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def perros(request):
    return render(request, 'core/perros.html')

def gatos(request):
    return render(request, 'core/gatos.html')

def aves(request):
    return render(request, 'core/aves.html')

def reptiles(request):
    return render(request, 'core/reptiles.html')

def peces(request):
    return render(request, 'core/peces.html')

def alimento(request):
    return render(request, 'core/alimento.html')

def camas(request):
    return render(request, 'core/camas.html')

def casas(request):
    return render(request, 'core/casas.html')

def correas(request):
    return render(request, 'core/correas.html')

def comederos(request):
    return render(request, 'core/comederos.html')

def limpieza(request):
    return render(request, 'core/limpieza.html')

def entrenamiento(request):
    return render(request, 'core/entrenamiento.html')

def farmacia(request):
    return render(request, 'core/farmacia.html')

def higiene(request):
    return render(request, 'core/higiene.html')

def juguetes(request):
    return render(request, 'core/juguetes.html')

def pulgas(request):
    return render(request, 'core/pulgas.html')

def regalos(request):
    return render(request, 'core/regalos.html')

def ropa(request):
    return render(request, 'core/ropa.html')

def premios(request):
    return render(request, 'core/premios.html')

def transporte(request):
    return render(request, 'core/transporte.html')

#gatos

def alimentogato(request):
    return render(request, 'core/alimentogato.html')

def camagato(request):
    return render(request, 'core/camagato.html')

def arenagato(request):
    return render(request, 'core/arenagato.html')

def snackgato(request):
    return render(request, 'core/snackgato.html')

def collaresgato(request):
    return render(request, 'core/collaresgato.html')
#
def farmaciagato(request):
    return render(request, 'core/farmaciagato.html')

def higienegato(request):
    return render(request, 'core/higienegato.html')

def juguetesgato(request):
    return render(request, 'core/juguetesgato.html')

def limpiezagato(request):
    return render(request, 'core/limpiezagato.html')

def pulgasgato(request):
    return render(request, 'core/pulgasgato.html')
#
def transportegato(request):
    return render(request, 'core/transportegato.html')

def ropagato(request):
    return render(request, 'core/ropagato.html')

def premiosgato(request):
    return render(request, 'core/premiosgato.html')

def rascadoresgato(request):
    return render(request, 'core/rascadoresgato.html')

#aves

def alimentoave(request):
    return render(request, 'core/alimentoave.html')

def comederoave(request):
    return render(request, 'core/comederoave.html')

def limpiezaave(request):
    return render(request, 'core/limpiezaave.html')

def entrenamientoave(request):
    return render(request, 'core/entrenamientoave.html')

def higieneave(request):
    return render(request, 'core/higieneave.html')

def jaulasave(request):
    return render(request, 'core/jaulasave.html')

def nidoave(request):
    return render(request, 'core/nidoave.html')

def perchasave(request):
    return render(request, 'core/perchasave.html')

def fundacion(request):
    return render(request, 'core/fundacion.html')

def formularioMascota(request):
    return render(request, 'core/formularioMascota.html')

#

def carrito_list(request):
    compra = compras.objects.all()
    contexto = {'compras':compra}
    return render(request, 'core/carrito.html', contexto)




def nuevoCliente(request):
    datos = {}
    if request.method == 'POST':
        formulario = CuentaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Cuenta creada!"
    else:
        datos['form'] = CuentaForm()
    form = CuentaForm()
    return render(request, 'core/crearCuenta.html', datos)

def ingresar(request):
    dato = {}
    if request.method == 'POST':
        formulario = validarUsuario(request.POST)
        if formulario.is_valid:
            dato['mensaje'] = "Bienvenido de vuelta!"
    else:
        dato['form'] = validarUsuario()
    form = validarUsuario()
    return render(request, 'core/ingresar.html', dato)

def animales(request):
    dato = {}
    if request.method == 'POST':
        formulario = animalesForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            dato['mensaje'] = "Mascota agregada."
    else:
        dato['form'] = animalesForm()
    form = animalesForm()
    return render(request, 'core/formularioMascota.html', dato)


def compras(request):
    dato = {}
    if request.method == 'POST':
        formulario = ComprasForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            dato['mensaje'] = "Se agregó al carrito!."
    else:
        dato['form'] = ComprasForm()
    form = ComprasForm()
    return render(request, 'core/compras.html', dato)   

