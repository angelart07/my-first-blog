from __future__ import unicode_literals

from django.db import models
from grados.models import Grado
from especialidades.models import Especialidad
from dependencias.models import Dependencia
from cursos.models import Curso

class Persona(models.Model):
	nombres = models.CharField(max_length=255, blank=False)
	apellidos = models.CharField(max_length=255, blank=False)
	cip = models.CharField(max_length=8, blank=False)
	dni = models.CharField(max_length=8, blank=False)
	grado = models.ForeignKey(Grado, blank=False)
	especialidad = models.ForeignKey(Especialidad, blank=False)
	dependencia = models.ForeignKey(Dependencia, blank=False)

	def __str__(self):
		return self.nombres.encode('utf-8')

	def get_absolute_url(self):
		return u'/personas/'

	

