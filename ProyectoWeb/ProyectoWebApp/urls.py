#from ProyectoWeb.settings import MEDIA_ROOT
from django.urls import path
from . import ViewsWebApp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', ViewsWebApp.HomeView.home,name="Home"),
    
    # Este proceso se tiene que crear independiente 
    #path('tienda', ViewsWebApp.HomeView.tienda,name="Tienda"),
    # Este proceso se tiene que crear independiente 
    path('contacto', ViewsWebApp.HomeView.contacto,name="Contacto"),
    ]

# es para ver los archivos de imagenes
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)