from django.shortcuts import render, HttpResponse
#from django.views.generic import TemplateView

# Create your views here.
#class IndexView(TemplateView):
#    template_name = 'index.html'

class HomeView():

        def home(request):
            return render(request,"ProyectoWebApp/home.html")


        # Tiene que ser de forma independeinte
        def tienda(request):
            return render(request,"ProyectoWebApp/tienda.html")


        # Tiene que ser de forma independeinte
        def contacto(request):
            return render(request,"ProyectoWebApp/contacto.html")

