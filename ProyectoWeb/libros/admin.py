# Register your models here.
from django.contrib import admin
from .models import *


class LibrosAdmin(admin.ModelAdmin):
    search_fields= ['titulo_libro','autor']
    list_display = ('titulo_libro','autor','grado')

admin.site.register(Tipo)
admin.site.register(Formato)
admin.site.register(Origen_Descarga)
admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Fuente)
admin.site.register(Grado)
admin.site.register(Clase)
admin.site.register(SubClase)
admin.site.register(Pais_Ciudad)
admin.site.register(Libros,LibrosAdmin)
