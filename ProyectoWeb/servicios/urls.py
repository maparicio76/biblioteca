#from ProyectoWeb.settings import MEDIA_ROOT
from django.urls import path
from . import views
# es para utilizar el setting y los static, esto para mostrar las imagenes
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('servicios', views.servicios,name="Servicios"),
    
    ]

