#from ProyectoWeb.settings import MEDIA_ROOT
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('libros', views.VLibros.libros,name="Libros"),
    path('buscar', views.VLibros.buscarlibro, name="Buscar"),
    path('buscarclase', views.VLibros.buscarlibroclase, name="BuscarClase"),
    path('clasemasoneria', views.VLibros.clasemasoneria, name="ClaseMasoneria"),
    path('clasereligiosos', views.VLibros.clasereligiosos, name="ClaseReligiosos"),
    
    #path('verificar_login',views.verificar_login),
    #path('registro', views.registro,name="Registro"),
    #path('registro', views.registro_view,name="Registro"),
    
    #path('busqueda_productos',views.busqueda_productos),

    ]

