
from django import forms
from django.forms import ModelForm
from ordenamiento.models import Parroquia, Barrio_Ciudadela


class ParroquiaForm(ModelForm): 
    class Meta:
        model = Parroquia
        fields = ['nombre', 'tipo_parroquia'] 

class BarrioCiudadelaForm(ModelForm):
    class Meta:
        model = Barrio_Ciudadela
        fields = ['nombre','num_viviendas','num_parques', 'num_edificios', 'parroquia']



class BarrioParroquiaForm(ModelForm): 
   
    #args tupla de opciones **kwarsg diccionario
    # Le 
    def __init__(self, parroquia, *args, **kwargs):
    #Constructor que hace referencia al self para sobreescribir el
    #constructor de model form
        super(BarrioParroquiaForm, self).__init__(*args, **kwargs)
        # darle un valor inicial a ese atributo
        # le asigna una parroquia y lo crea como hidden o oculto
        # se agrega el objeto parroquia asociada
        self.initial['parroquia'] = parroquia
        # darle a parroquia un widget que hace generar un forms
        # para generar un input ociulto
        self.fields["parroquia"].widget = forms.widgets.HiddenInput()
        print(parroquia)
    
    class Meta:
        model = Barrio_Ciudadela 
        fields = ['nombre','num_viviendas','num_parques', 'num_edificios', 'parroquia'] 