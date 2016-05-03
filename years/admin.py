from django.contrib import admin

from .models import Year

@admin.register(Year)
class YearAdmin(admin.ModelAdmin):
	list_display = ('year',)