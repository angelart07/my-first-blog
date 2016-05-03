from __future__ import unicode_literals

from django.db import models
from docentes.models import Docente

class Curso(models.Model):
	curso = models.CharField(max_length=255)
	codigo = models.CharField(max_length=10)
	docente = models.OneToOneField(Docente)
	vacantes = models.PositiveIntegerField(default=0)
	fecha_de_inicio = models.DateField()
	fecha_de_termino = models.DateField()

	def __str__(self):
		return self.curso.encode('utf-8')

	def get_absolute_url(self):
		return u'/cursos/'