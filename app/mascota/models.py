from __future__ import unicode_literals

from django.db import models

from app.adopcion.models import Persona

class Vacuna(models.Model):
    nombre = models.CharField(max_length=50)


class Mascota(models.Model):
    nombre = models.CharField(max_length=50)
    sexo = models.CharField(max_length=10)
    edad_aproximada = models.IntegerField()
    fecha_rescate = models.DateField()
    persona = models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
    vacuna = models.ManyToManyField(Vacuna, blank=True)

    def __str__(self):
        return '{}'.format(self.nombre)  #cuando acceda a mi objeto, pueda verse por el nombre