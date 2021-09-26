from django.db import models
from django.db.models.base import Model

# Create your models here.


class Gran_oriente (models.Model):
    id_gran_oriente = models.AutoField(primary_key=True)
    nombre_gran_oriente = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        verbose_name='gran_oriente'
        verbose_name_plural='gran_orientes'

    def __str__(self):
        return self.nombre_gran_oriente      

class Oriente (models.Model):
    id_oriente = models.AutoField(primary_key=True)
    nombre_oriente = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        verbose_name='oriente'
        verbose_name_plural='orientes'

    def __str__(self):
        return self.nombre_oriente 

class Valle (models.Model):
    id_valle = models.AutoField(primary_key=True)
    nombre_valle = models.CharField(max_length=50, null=False, blank=False)
    oriente = models.ForeignKey(Oriente, null=False, blank=False, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='valle'
        verbose_name_plural='valles'

    def __str__(self):
        return self.nombre_valle

class Rito (models.Model):
    id_rito = models.AutoField(primary_key=True)
    nombre_rito = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        verbose_name='rito'
        verbose_name_plural='ritos'

    def __str__(self):
        return self.nombre_rito


class Pais (models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=50, null=False, blank=False)
    
    class Meta:
        verbose_name='pais'
        verbose_name_plural='paises'

    def __str__(self):
        return self.nombre_pais


class Ciudad (models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=50, null=False, blank=False)
    pais = models.ForeignKey(Pais, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name='ciudad'
        verbose_name_plural='ciudades'

    def __str__(self):
        return self.nombre_ciudad


class Logia (models.Model):
    id_logia = models.AutoField(primary_key=True)
    nombre_logia = models.CharField(max_length=50, null=False, blank=False)
    nro_logia  = models.IntegerField()
    gran_oriente = models.ForeignKey(Gran_oriente, null=True, blank=False, on_delete=models.CASCADE)
    valle = models.ForeignKey(Valle, null=False, blank=False, on_delete=models.CASCADE) 
    rito = models.ForeignKey(Rito, null=False, blank=False, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, null=False, blank=False, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name='logia'
        verbose_name_plural='logias'
    def __str__(self):
        txt = "ID Logia : {0}, Nombre Logia :  {1}, Numero Logia : {2}  "
        return txt.format(self.id_logia,self.nombre_logia,self.nro_logia)


class Grado (models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre_grado = models.CharField(max_length=10, null=False, blank=False)
    
    class Meta:
        verbose_name='grado'
        verbose_name_plural='grados'

    def __str__(self):
        return self.nombre_grado
    
class Usuarios(models.Model):
    id_usuarios = models.AutoField(primary_key=True)
    login_usuario = models.CharField(max_length=15, null=False, blank=False)
    password_usuario = models.CharField(max_length=15, null=False, blank=False)
    nombres = models.CharField(max_length=50, null=False, blank=False)
    apellidos = models.CharField(max_length=100, null=False, blank=False)
    ncelular = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)    
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_grado = models.DateField()
    grado = models.ForeignKey(Grado, null=False, blank=False, on_delete=models.CASCADE)
    logia = models.ForeignKey(Logia, null=False, blank=False, on_delete=models.CASCADE)
    

    def __str__(self):
        txt = "ID Usuario : {0}, Login :  {1}, Password : {2}, Nombre : {3}, Apellidos : {4}, Nro Celular : {5}, Email :{6}"
        return txt.format(self.id_usuarios,self.login_usuario,self.password_usuario,self.nombres,self.apellidos,self.ncelular,self.email)


