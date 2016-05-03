from __future__ import unicode_literals

from django.db import models


class Grado(models.Model):
	grado = models.CharField(max_length=3)
	descripcion = models.CharField(max_length=255)

	def __str__(self):
		return self.grado.encode('utf-8')

	def get_absolute_url(self):
		return u'/grados/'