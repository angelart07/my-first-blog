from __future__ import unicode_literals

from django.db import models

class Dependencia(models.Model):
	nombre = models.CharField(max_length=255)
	descripcion = models.CharField(max_length=255)

	def __str__(self):
		return self.nombre.encode('utf-8')

	def get_absolute_url(self):
		return u'/dependencias/'