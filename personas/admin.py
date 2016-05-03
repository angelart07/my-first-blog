from django.contrib import admin

from .models import Persona

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ('nombres',
					'apellidos',
					'cip',
					'dni',
					'grado',
					'especialidad', 
					'dependencia',
					'curso', )
	
	list_filter = ('especialidad',)


	 