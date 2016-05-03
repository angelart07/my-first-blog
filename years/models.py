from __future__ import unicode_literals

from django.db import models

class Year(models.Model):
	year = models.IntegerField()

	def __str__(self):
		return str(self.year)

	def get_absolute_url(self):
		return u'/years/'