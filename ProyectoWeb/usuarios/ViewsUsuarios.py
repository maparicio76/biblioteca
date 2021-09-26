from typing import ContextManager
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
#from .models import Usuarios
from .models import *
from .forms import *

# Funsion de Login de Usuario

class VUsuario():

        def Ulogin(request): 
            return render(request,"usuarios/login.html")    

### VERIFICACION DE AUTHENTICACION   
        def verificar_login(request):
            u_login = request.GET["u_login"]
            u_password = request.GET["u_password"]
              
            #contraseña01 = str(datos_u.values('password_usuario'))
            #ESTA CONSULTA ME DA EL CAMPO PASSWORD DE LA TUPLA
            datos_u = Usuarios.objects.filter(login_usuario = u_login) 
            
            for datos in datos_u:
                u_celular = datos.ncelular
                u_email = datos.email
                u_idusuario = datos.id_usuarios
               #u_nombres = datos.nombres

            datos_passw = datos_u.filter(password_usuario = u_password)
            #datos_ncelular = datos_u.filter(ncelular__contains = "vacio")
            #datos_mail = datos_u.filter(email__contains = "vacio")    

            if datos_u:
                if datos_passw:
                    if u_celular in "ninguno":
                        mensaje = " FALTAN DATOS POR COMPLETAR CELULAR: del usuario : %r" %u_celular
                        dato_usuario = Usuarios.objects.get(id_usuarios = u_idusuario)
                        form = UsuarioLogiaForm(instance=dato_usuario)  
                        return render(request, 'usuarios/u_edicion.html', {'form':form})                
                    else:
                        if u_email in "ninguno":
                            mensaje = " FALTAN DATOS POR COMPLETAR EMAIL : del usuario : %r" %u_email                       
                            dato_usuario = Usuarios.objects.get(id_usuarios = u_idusuario)
                            form = UsuarioLogiaForm(instance=dato_usuario)  
                            return render(request, 'usuarios/u_edicion.html', {'form':form})                
                        else:                             
                            #return render(request, "libros/buscar_libro.html", {'form':u_nombres})
                            return render(request, "libros/buscar_libro.html")
                            #mensaje = " DATOS CORRECTOS Y LLENADOS : del usuario : %r" %u_login


                else:
                    #mensaje = " CONTRASEÑA ERRONEA : del usuario : %r" %u_login                
                    mensaje = " CONTRASEÑA ERRONEA "
            else:         
                #mensaje = " EL USUARIO NO NO EXISTE :  %r" %u_login
                mensaje = " EL USUARIO NO NO EXISTE "

            return render(request, "usuarios/login.html",{"mensaje":mensaje})
                #return redirect_class(resolve_url(to, *args, **kwargs)) 
   
    
        # PUEDO MODIFICAR EL form por uform para identificarlo
        ####### FUNCION DE REGISTRO DE USUARIO
        def registro(request):
            if request.method == 'POST':
                form = UsuarioLogiaForm(request.POST)
                if form.is_valid():
                    form.save()
                return render(request,"usuarios/u_registrado.html")
                
            else:
                form = UsuarioLogiaForm()
           
            return render(request, 'usuarios/registro.html', {'form':form})
        
        ########################################################
       
        def usuario_edit(request):

            if request.method == 'POST':
                    form = UsuarioLogiaForm(request.POST)
                    if form.is_valid():
                        form.save()
                    return render(request,"usuarios/u_registrado.html")
                    
            else:
                 dato_usuario = Usuarios.objects.get(id_usuarios = 1)
                 form = UsuarioLogiaForm(instance=dato_usuario)
                 #return render(request, 'usuarios/registro.html', {'form':form})
                 #form = UsuarioLogiaForm()
           
            return render(request, 'usuarios/u_edicion.html', {'form':form})
             
               

        def busqueda_productos(request):
            return render(request, "usuarios/busqueda_productos.html")


        def buscar(request):

            mensaje=" EL USUARIO EXISTE %r" %request.GET["usu"]

            return HttpResponse(mensaje)
        

         #########################################################

        #def editar (request,id_usuario):
        #    d_usuario = LogiaUsuarios.objects.filter(login_usuario = id_usuario).first()
        #    form = UsuarioLogiaForm(instance=d_usuario)
        #    return render(request, 'usuarios/u_edicion.html', {'form':form,'d_usuario':d_usuario})

