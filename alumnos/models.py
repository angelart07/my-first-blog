from __future__ import unicode_literals

from django.db import models
from personas.models import Persona
from cursos.models import Curso

class Alumno(models.Model):
	persona = models.ForeignKey(Persona, blank=False)
	cip = persona.cip
	curso = models.ForeignKey(Curso, blank=False)

	def __str__(self):
		return self.nombres.encode('utf-8')

	def get_absolute_url(self):
		return u'/alumnos/'

	

