from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm, PostForm
from django.contrib import messages


def registro(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('feed')
	else:
		form = UserRegisterForm()

	context = { 'form' : form }
	return render(request, 'tierra/registro.html', context)



def tienda(request):
    return render(request,'tierra/tienda.html')
def usuario(request):
    return render(request, 'tierra/usuario.html')

def productos_plantas(request):
    return render(request, 'tierra/productos_plantas.html')

def productos_maceteros(request):
    return render(request, 'tierra/productos_maceteros.html')

def productos_tierra(request):
    return render(request, 'tierra/productos_tierra.html')

def productos_mangueras(request):
    return render(request, 'tierra/productos_mangueras.html')

def productos_herramientas(request):
    return render(request, 'tierra/productos_herramientas.html')

def productos_arbustos(request):
    return render(request,'tierra/productos_arbustos.html')

def manguera_goteo(request):
    return render(request,'tierra/manguera_goteo.html')

def tierra_macetero_tamizada(request):
    return render(request,'tierra/tierra_macetero_tamizada.html')

def tierra_acida(request):
    return render(request,'tierra/tierra_acida.html')

def arbusto_mariposa(request):
    return render(request,'tierra/arbusto_mariposa.html')

def inicio(request):
    return render(request,'tierra/inicio.html')

def arbustos(request):
    return render(request,'tierra/arbustos.html')

def autorriego(request):
    return render(request,'tierra/autorriego.html')

def azadilla(request):
    return render(request,'tierra/azadilla.html')

def boj(request):
    return render(request,'tierra/boj.html')

def carrito(request):
    return render(request,'tierra/carrito.html')

def ceramica(request):
    return render(request,'tierra/ceramica.html')

def colgante(request):
    return render(request,'tierra/colgante.html')

def contacto(request):
    return render(request,'tierra/contacto.html')

def cultivador(request):
    return render(request,'tierra/cultivador.html')

def Forsythia(request):
    return render(request,'tierra/Forsythia.html')

def geranios(request):
    return render(request,'tierra/geranios.html')

def helecho(request):
    return render(request,'tierra/helecho.html')

def herramientas(request):
    return render(request,'tierra/herramientas.html')

def laurel(request):
    return render(request,'tierra/laurel.html')

def lavanda(request):
    return render(request,'tierra/lavanda.html')

def libutrina(request):
    return render(request,'tierra/libutrina.html')

def lirio(request):
    return render(request,'tierra/lirio.html')
def login(request):
    return render(request,'tierra/login.html')

def macetero_mimbre(request):
    return render(request,'tierra/macetero_mimbre.html')

def manguera_alta_presion(request):
    return render(request,'tierra/manguera_alta_presion.html')

def manguera_aspersion(request):
    return render(request,'tierra/manguera_aspersion.html')

def Manguera_estandar(request):
    return render(request,'tierra/Manguera_estandar.html')

def manguera_expandible(request):
    return render(request,'tierra/manguera_expandible.html')

def manguera_subterraneo(request):
    return render(request,'tierra/manguera_subterraneo.html')

def mangueras(request):
    return render(request,'tierra/mangueras.html')

def modificar_contrasena(request):
    return render(request,'tierra/modificar_contrasena.html')

def nosotros(request):
    return render(request,'tierra/nosotros.html')

def maceteros(request):
    return render(request,'tierra/maceteros.html')

def pala(request):
    return render(request,'tierra/pala.html')

def petunias(request):
    return render(request,'tierra/petunias.html')

def plantador(request):
    return render(request,'tierra/plantador.html')

def plantas(request):
    return render(request,'tierra/plantas.html')

def plastico(request):
    return render(request,'tierra/plastico.html')

def rastrillo(request):
    return render(request,'tierra/rastrillo.html')

def recuperar_contrasena(request):
    return render(request,'tierra/recuperar_contrasena.html')

def registro(request):
    return render(request,'tierra/registro.html')

def rosa(request):
    return render(request,'tierra/rosa.html')

def rosas(request):
    return render(request,'tierra/rosas.html')


def terracota(request):
    return render(request,'tierra/terracota.html')

def terratierra_acidacota(request):
    return render(request,'tierra/tierra_acida.html')

def tierra_enriquecida(request):
    return render(request,'tierra/tierra_enriquecida.html')

def tierra_hoja(request):
    return render(request,'tierra/tierra_hoja.html')

def terracotierra_macetero_tamizadata(request):
    return render(request,'tierra/tierra_macetero_tamizada.html')

def tierra_maceteros(request):
    return render(request,'tierra/tierra_maceteros.html')

def tierra_normal(request):
    return render(request,'tierra/tierra_normal.html')

def tierra_tamizada(request):
    return render(request,'tierra/tierra_tamizada.html')

def tijeras(request):
    return render(request,'tierra/tijeras.html')

def ver_perfil_de_usuario(request):
    return render(request,'tierra/ver_perfil_de_usuario.html')