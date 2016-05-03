from django.contrib import admin
from .models import Alumno

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
	list_display = ('nombres',
					'apellidos',
					'cip',
					'dni',
					'grado',
					'especialidad', 
					'dependencia',
					'curso', )
	
	list_filter = ('especialidad',)

	 
	 
	 
	 
	 
	 