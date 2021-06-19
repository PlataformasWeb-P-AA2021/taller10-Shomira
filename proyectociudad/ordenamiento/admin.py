from django.contrib import admin


# Importar las clases del modelo
from ordenamiento.models import Parroquia, Barrio_Ciudadela

# Clase que hereda de un modeloAdmin para el modelo Parroquia
class ParroquiaAdmin(admin.ModelAdmin):

    # Listado de atributos que se mostrará por cada registro
    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre', 'tipo_parroquia')

#admin.site se le envia como primer argumento el modelo Parroquia
# y el segundo argumento la clase ParroquiaAdmin
admin.site.register(Parroquia, ParroquiaAdmin)


class Barrio_CiudadelaAdmin(admin.ModelAdmin):

    # listado de atributos que se mostrará por cada registro 
    list_display = ('nombre', 'num_viviendas', 'num_edificios', 'num_parques', 'parroquia')
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio_Ciudadela, Barrio_CiudadelaAdmin)