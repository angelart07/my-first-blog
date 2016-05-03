from __future__ import unicode_literals

from django.db import models
from grados.models import Grado
from especialidades.models import Especialidad
from dependencias.models import Dependencia

class Docente(models.Model):
	nombres = models.CharField(max_length=255, blank=False)
	apellidos = models.CharField(max_length=255, blank=False)
	cip = models.CharField(max_length=8, blank=False)
	dni = models.CharField(max_length=8, blank=False, )
	grado = models.ForeignKey(Grado, blank=False, related_name="Grado")
	especialidad = models.ForeignKey(Especialidad, blank=False, verbose_name="Especialidad")
	dependencia = models.ForeignKey(Dependencia, blank=False, related_name="Dependencia")

	def __str__(self):
		apellidos = self.apellidos.split(" ")
		apellido1 = apellidos[0]
		docente = u'%s %s %s'% (self.grado, self.especialidad, apellido1)
		return docente.encode('utf-8').upper()

	def get_absolute_url(self):
		return u'/docentes/'