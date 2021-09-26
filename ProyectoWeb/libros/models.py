# Create your models here.
from django.db import models
from django.db.models.base import Model
# Create your models here.




class Pais_Ciudad (models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre_pais = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='pais'
        verbose_name_plural='paises'
    def __str__(self):
        return self.nombre_pais


class Clase (models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre_clase = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='clase'
        verbose_name_plural='clases'
    def __str__(self):
        return self.nombre_clase

class SubClase (models.Model):
    id_subclase = models.AutoField(primary_key=True)
    nombre_subclase = models.CharField(max_length=50, null=False, blank=False)
    clase = models.ForeignKey(Clase, null=False, blank=False, on_delete=models.CASCADE)
    class Meta:
        verbose_name='subclase'
        verbose_name_plural='subclases'
    def __str__(self):
        return self.nombre_subclase


class Grado (models.Model):
    id_grado = models.AutoField(primary_key=True)
    nombre_grado = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='grado'
        verbose_name_plural='grados'
    def __str__(self):
        return self.nombre_grado


class Fuente (models.Model):
    id_fuente = models.AutoField(primary_key=True)
    nombre_fuente = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='fuente'
        verbose_name_plural='fuentes'
    def __str__(self):
        return self.nombre_fuente 


class Autor (models.Model):
    id_autor = models.AutoField(primary_key=True)
    nombre_autor = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='autor'
        verbose_name_plural='autores'
    def __str__(self):
        return self.nombre_autor 


class Editorial (models.Model):
    id_editorial = models.AutoField(primary_key=True)
    editorial = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='editorial'
        verbose_name_plural='editoriales'
    def __str__(self):
        return self.editorial 


class Origen_Descarga (models.Model):
    id_origen = models.AutoField(primary_key=True)
    origen_descarga = models.CharField(max_length=50, null=False, blank=False)
    class Meta:
        verbose_name='origen descarga'
        verbose_name_plural='origen descargas'
    def __str__(self):
        return self.origen_descarga 


class Formato (models.Model):
    id_formato = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=10, null=False, blank=False)
    class Meta:
        verbose_name='formato'
        verbose_name_plural='formatos'
    def __str__(self):
        return self.tipo 


class Tipo (models.Model):
    id_tipo = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, null=False, blank=False)
    class Meta:
        verbose_name='tipo'
        verbose_name_plural='tipos'
    def __str__(self):
        return self.tipo 


class Libros (models.Model):
    id_libro = models.AutoField(primary_key=True)
    titulo_libro = models.CharField(max_length=50)
    isbn = models.CharField(max_length=30)
    anho_edicion = models.DateField()
    fecha_alta_registro =  models.DateTimeField(auto_now_add=True)
    observacion = models.CharField(max_length=100)
    libro_fuente = models.FileField(upload_to='libro_fuente/',null=True,blank=True)

    tipo = models.ForeignKey(Tipo, null=False, blank=False, on_delete=models.CASCADE)
    formato = models.ForeignKey(Formato, null=False, blank=False, on_delete=models.CASCADE)
    origen_descarga = models.ForeignKey(Origen_Descarga, null=False, blank=False, on_delete=models.CASCADE)
    editorial = models.ForeignKey(Editorial, null=False, blank=False, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, null=False, blank=False, on_delete=models.CASCADE)
    fuente = models.ForeignKey(Fuente, null=False, blank=False, on_delete=models.CASCADE)
    grado = models.ForeignKey(Grado, null=False, blank=False, on_delete=models.CASCADE)
    subclase = models.ForeignKey(SubClase, null=False, blank=False, on_delete=models.CASCADE)
    pais_ciudad = models.ForeignKey(Pais_Ciudad, null=False, blank=False, on_delete=models.CASCADE)    
    def __str__(self):
        txt = "ID Libro : {0}, Titulo :  {1}, ISBN : {2}, Año Edicion : {3}, Fecha Registro : {4}, Observacion : {5}, Libro : {6} "
        return txt.format(self.id_libro,self.titulo_libro,self.isbn,self.anho_edicion,self.fecha_alta_registro,self.observacion,self.libro_fuente)

    
