from typing import Match
from django.db import models
from django.db.models.fields import TextField
#from django.db.models.fields import BooleanField
from django.utils import timezone


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
	categoria = models.CharField(max_length=100, blank=True, null=True)
	contenido = models.TextField()
	

	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def _str_(self):
		return self.titulo
	
	class Meta:
		verbose_name =("Post")
		verbose_name_plural =("Posts")        

  

class Persona(ModeloBase):
	nombre = models.CharField(max_length=200)
	email = models.CharField(max_length=200)

class Comentario(ModeloBase):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	autor = models.CharField(Persona, max_length=200, unique=True)
	titulo = models.CharField(max_length=200, unique=True)
	contenido = models.TextField()
	
	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def _str_(self):
		return self.autor

	class Meta:
		verbose_name_plural =("Comentarios")
		verbose_name=('Comentario') 



    	




# Create your models here.

# class ModeloBase(models.Model):
#     id = models.AutoField(primary_key=True)
#     estado = models.BooleanField('Estado', default=True)
#     fecha_creacion=models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
#     fecha_eliminacion=models.DateField('Fecha de eliminación', auto_now=True, auto_now_add=False)
#     fecha_modificacion=models.DateField('Fecha de modificación', auto_now=True, auto_now_add=False)

#     class Meta:
#         abstract = True

# class Post(ModeloBase):
    
# 	autor = models.CharField(max_length=200, unique=True)
# 	titulo = models.CharField(max_length=200, unique=True)
# 	categoria = models.CharField(max_length=100, blank=True, null=True)
# 	contenido = models.TextField()
	

# 	def publicar(self):
# 		self.fecha_publicacion= timezone.now()
# 		self.save()

# 	def _str_(self):
# 		return self.titulo
	
# 	class Meta:
# 		verbose_name =("Post")
# 		verbose_name_plural =("Posts")        

  

# class Comentario(ModeloBase):
# 	post = models.ForeignKey(Post, on_delete=models.CASCADE)
# 	autor = models.CharField(Persona, max_length=200, unique=True)
# 	titulo = models.CharField(max_length=200, unique=True)
# 	contenido = models.TextField()
	

# 	def publicar(self):
# 		self.fecha_publicacion= timezone.now()
# 		self.save()

# 	def _str_(self):
# 		return self.autor

# 	class Meta:
    	
# 		verbose_name_plural =("Comentarios")
# 		verbose_name=('Comentario') 

# class Persona(ModeloBase):
#     nombre=models.CharField(max_length=200)
# 	email=models.CharField(max_length=200)
# 	perro=TextField()

    	
    




      # def getComentario(self):
        #     if self.comentario.all():
        #         return self.comentario.all()
        #     else:
        #         return None