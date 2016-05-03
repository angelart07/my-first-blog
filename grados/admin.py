from django.contrib import admin
from .models import Grado


@admin.register(Grado)
class GradoAdmin(admin.ModelAdmin):
	list_display = ('grado', 'descripcion',)
