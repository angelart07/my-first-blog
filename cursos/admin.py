from django.contrib import admin
from .models import Curso

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
	list_display = ('curso',
					'codigo',
					'docente',
					'vacantes',
					'fecha_de_inicio',
					'fecha_de_termino',)
