from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class LibroForm(forms.ModelForm):

       class Meta:
              model = Libros

              fields = [
                    
                    'titulo_libro',
                    
    
              ]
              label = {
                    
                    'titulo_libro':'Titulo',
                    
    
              }

              widgets = {
                    
                    'titulo_libro':forms.TextInput(attrs={'class':'form-control'}), 
                    
    
              }
