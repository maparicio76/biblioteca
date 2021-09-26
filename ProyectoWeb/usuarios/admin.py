from django.contrib import admin
#from import_export import resources
#from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import *


class CategoriaAdmin(admin.ModelAdmin):
    search_fields= ['nombres','apellidos']
    list_display = ('nombres','apellidos','logia')


admin.site.register(Gran_oriente)
admin.site.register(Oriente)
admin.site.register(Valle)
admin.site.register(Logia)
admin.site.register(Rito)
admin.site.register(Pais)
admin.site.register(Grado)
admin.site.register(Ciudad)
admin.site.register(Usuarios,CategoriaAdmin)

