# Generated by Django 3.2.4 on 2021-06-19 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Parroquia')),
                ('tipo_parroquia', models.CharField(choices=[('Urbana', 'Urbana '), ('Rural', 'Rural')], max_length=30, verbose_name='Ubicación de Parroquia')),
            ],
        ),
        migrations.CreateModel(
            name='Barrio_Ciudadela',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre Barrio o Ciudadela')),
                ('num_viviendas', models.IntegerField(verbose_name='Número de viviendas')),
                ('num_edificios', models.IntegerField(verbose_name='Número de edificios')),
                ('num_parques', models.IntegerField(choices=[(1, 'Un parque'), (2, 'Dos parques'), (3, 'Tres parques'), (4, 'Cuatro parques'), (5, 'Cinco parques'), (6, 'Seis parques')], verbose_name='Numero de Parques')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parroquia', to='ordenamiento.parroquia')),
            ],
        ),
    ]
