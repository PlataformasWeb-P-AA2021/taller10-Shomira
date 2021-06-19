"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from.import views


urlpatterns = [
        path('', views.index, name='index'),
        path('listadoParroquias', views.listadoParroquias, 
            name='listadoParroquias'),
        path('listadoBarrios', views.listadoBarrios, 
            name='listadoBarrios'),
        path('crear/Parroquia', views.crearParroquia, 
            name='crearParroquia'),
        path('crear/BarrioParroquia/<int:id>', views.crearBarrioParroquia, 
            name='crearBarrioParroquia'),
        path('editar/Parroquia/<int:id>', views.editarParroquia, 
            name='editarParroquia'),
        path('editar/Barrio/<int:id>', views.editarBarrio, 
            name='editarBarrio'),
      
 ]