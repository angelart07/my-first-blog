from django.contrib import admin

from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
	list_display = ('nombres',
					'apellidos',
					'cip',
					'dni',
					'grado',
					'especialidad', 
					'dependencia',
					'curso', )
	
	list_filter = ('especialidad',)


	 