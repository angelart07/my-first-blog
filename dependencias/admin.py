from django.contrib import admin
from .models import Dependencia

@admin.register(Dependencia)
class DependenciaAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'descripcion',)
