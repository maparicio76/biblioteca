from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class UsuarioLogiaForm(forms.ModelForm):

                    

       class Meta:

            
              model = Usuarios

              fields = [
                    'login_usuario', 
                    'password_usuario',
                    'nombres',
                    'apellidos',
                    'ncelular',
                    'email',
                    'fecha_grado',
                    'logia', 
                    'grado',
                    
                        
              ]
              label = {
                    'login_usuario':'Login', 
                    'password_usuario':'Contraseña',
                    'nombres':'Nombres',
                    'apellidos':'Apellidos',
                    'ncelular':'Nro Celular',
                    'email':'Correro',
                    'fecha_grado':'Fecha Grado',
                    'logia':'Logia',
                    'grado':'Grado', 
                    
    
              }

              widgets = {
                    'login_usuario':forms.TextInput(attrs={'class':'form-control'}), 
                    'password_usuario':forms.TextInput(attrs={'class':'form-control'}), 
                    'nombres':forms.TextInput(attrs={'class':'form-control'}), 
                    'apellidos':forms.TextInput(attrs={'class':'form-control'}), 
                    'ncelular':forms.TextInput(attrs={'class':'form-control'}), 
                    'email':forms.TextInput(attrs={'class':'form-control'}), 
                    'fecha_grado':forms.DateInput(attrs={'class':'form-control'}),
                    'logia': forms.Select(attrs={'class':'form-control'}),          
                    'grado':forms.Select(attrs={'class':'form-control'}),
                   
                        
              }


