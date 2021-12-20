from django.db import models
#from django.db.models.fields import BooleanField
from django.utils import timezone


# Create your models here.

class ModeloBase(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    fecha_eliminacion=models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)
    fecha_modificacion=models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

class Post(ModeloBase):
    
	autor = models.CharField(max_length=200, unique=True)
	titulo = models.CharField(max_length=200, unique=True)
	contenido = models.TextField()
	

	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def _str_(self):
		return self.titulo

	class Meta:
		verbose_name =("Post")
		verbose_name_plural =("Posts")        

class Comentario(ModeloBase):
	autor = models.CharField(max_length=200, unique=True)
	titulo = models.CharField(max_length=200, unique=True)
	contenido = models.TextField()
	

	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def _str_(self):
		return self.titulo

	class Meta:
		verbose_name =("Comentario")
		verbose_name_plural =("Comentarios") 

