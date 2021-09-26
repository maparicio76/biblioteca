
# Create your views here.
from typing import ContextManager
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
#from .models import Libros
from .models import *
from .forms import *



# Funsion de Login de Usuario

class VLibros():


    def libros(request):    
        
        return render(request,"libros/buscar_libro.html")   

    def buscarlibro(request):    
        l_titulo = request.GET["buscar"]
        
        datoslibro = Libros.objects.filter(titulo_libro__contains = l_titulo)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/buscar_libro.html', {'form':datoslibro})                
        else:
            return render(request,"libros/buscar_libro.html")
 
    # LA PAGINA PRINCIPAL DE LA CLASE
    #def buscarlibroclase(request,nombreclase):    
    def buscarlibroclase(request):        
        nombreclase = "maximo" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/buscar_libro_clase.html', {'form':datoslibro})                
        else:
            return render(request,"libros/buscar_libro_clase.html")

    
    def clasemasoneria(request):        
        nombreclase = "MASONERIA" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/clase_masoneria.html', {'form':datoslibro})                
        else:
            return render(request,"libros/clase_masoneria.html")
    
    def clasereligiosos(request):        
        nombreclase = "maximo" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/clase_religiosos.html', {'form':datoslibro})                
        else:
            return render(request,"libros/clase_religiosos.html")

    def clasecivilizaciones(request):        
        nombreclase = "maximo" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/clase_masoneria.html', {'form':datoslibro})                
        else:
            return render(request,"libros/clase_masoneria.html")
    
    def claseuniverso(request):        
        nombreclase = "maximo" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/clase_masoneria.html', {'form':datoslibro})                
        else:
            return render(request,"libros/clase_masoneria.html")
    
    def clasefilosofia(request):        
        nombreclase = "maximo" 
        
        datoslibro = Libros.objects.filter(titulo_libro = nombreclase)
        #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")

        if datoslibro:
            return render(request, 'libros/clase_masoneria.html', {'form':datoslibro})                
        else:
            return render(request,"libros/clase_masoneria.html")
    