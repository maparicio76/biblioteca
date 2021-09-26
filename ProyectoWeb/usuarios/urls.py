#from ProyectoWeb.settings import MEDIA_ROOT
from django.urls import path
from . import ViewsUsuarios
#from django.conf import settings
from django.conf.urls.static import static

# agregados para utilizar el login
from django.contrib.auth.views import LoginView,logout_then_login

urlpatterns = [
    
    path('login', ViewsUsuarios.VUsuario.Ulogin,name="Usuarios"),
    path('verificar_login',ViewsUsuarios.VUsuario.verificar_login),
    path('registro', ViewsUsuarios.VUsuario.registro,name="Registro"),
    #path('usuario_edit', ViewsUsuarios.VUsuario.usuario_edit,name="usuario_edit"),
    #path('editarUsuarios/<int:id_usuario>', ViewsUsuarios.VUsuario.editar,name="editarUsuarios"),
    
    
    
    
    
    #path('registro', views.registro_view,name="Registro"),
    #path('buscar',views.buscar),
    #path('busqueda_productos',views.busqueda_productos),

    ]

