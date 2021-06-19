from django.db import models
# Create your models here.

class Parroquia(models.Model):
    #Opciones Parroquia
    tipo_parroquia = (
        ('Urbana', 'Urbana '),
        ('Rural', 'Rural'),
        )
    nombre = models.CharField("Nombre Parroquia",max_length=50)
    tipo_parroquia = models.CharField("Ubicación de Parroquia",max_length=30, \
            choices=tipo_parroquia) 


    def __str__(self):
        return "Nombre Parroquia: %s \n Tipo parroquia : %s" % (
                self.nombre,
                self.tipo_parroquia)


class Barrio_Ciudadela(models.Model):
    #Opciones de Parques
    num_parques = (
        (1,'Un parque'),
        (2,'Dos parques'),
        (3,'Tres parques'),
        (4,'Cuatro parques'),
        (5,'Cinco parques'),
        (6,'Seis parques'),
    )

    nombre = models.CharField("Nombre Barrio o Ciudadela",max_length=50)
    num_viviendas = models.IntegerField("Número de viviendas")
    num_edificios = models.IntegerField("Número de edificios")
    num_parques = models.IntegerField("Numero de Parques", \
            choices= num_parques)
    parroquia = models.ForeignKey(Parroquia, on_delete=models.CASCADE, \
    related_name="barrios")


    def __str__(self):
        return "Nombre: %s - Número Viviendas: %d - Número Edificios: %d - Numero parques: %d " % (self.nombre, 
                self. num_viviendas,
                self.num_edificios,
                self.num_parques)