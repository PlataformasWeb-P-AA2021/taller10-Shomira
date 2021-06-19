from django.shortcuts import redirect, render
from ordenamiento.models import Parroquia, Barrio_Ciudadela
# importar los formularios de forms.py 
from ordenamiento.forms import ParroquiaForm, BarrioCiudadelaForm, BarrioParroquiaForm

def index(request):
    parroquias = Parroquia.objects.all()

    informacion_template = {'Parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)



def listadoParroquias(request):
    """
    Listar los registros del modelo Parroquia, 
    obtenidos de la base de datos.
    """
    # a través del ORM de django se obtiene
    # los registros de la entidad; el listado obtenido
    # se lo almacena en una variable llamada
    # parroquias
    parroquias = Parroquia.objects.all()
    
    # en la variable tipo diccionario llamada informacion_template
    # se agregará la información que estará disponible
    # en el template
    informacion_template = {'parroquias': parroquias}
    return render(request, 'listadoParroquias.html', informacion_template)

# Generar una vista que liste los barrios 
def listadoBarrios(request):
    
    barrios = Barrio_Ciudadela.objects.all()
   
   
    informacion_template = {'barrios': barrios,  'numero_barrios' : len(barrios)}
    return render(request, 'listadoBarrios.html', informacion_template)
    
#Generar un formulario que cree una parroquia

def crearParroquia(request):
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario) 

#Generar un formulario que cree un barrio de una parroquia
def crearBarrioParroquia(request, id):

    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        # No se envia una instancia sino un objeto
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'estudiante': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario) 


#Generar un formulario que edite una parroquia
def editarParroquia(request, id):
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario) 

#Generar un formulario que edite un barrio
def editarBarrio(request, id):
    """
    """
    barrio =Barrio_Ciudadela.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioCiudadelaForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        #Envia la instancia de tipo telefono, da el formulario cargado
        #
        formulario = BarrioCiudadelaForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario) 

