from django.db import models
from django.core.urlresolvers import reverse

class Category(models.Model):
    """ Categorias para clasificar las fotos """
    name = models.CharField(max_length=50)
    def __str__(self):             
        return self.name

class Photo(models.Model):
	"""Fotos del album"""
	category=models.ForeignKey(Category,null=True,blank=True)
	title=models.CharField(max_length=50,default='No title')
	photo=models.ImageField(upload_to='photos/')
	pub_date=models.DateField(auto_now_add=True)
	favorite=models.BooleanField(default=False)
	comment=models.CharField(max_length=200,blank=True)
	"""metodo que permite que una vez que se actualice la foto se pueda volver a recargar el template en este caso se envia a la lista de fotos"""
	def get_absolute_url(self):
		return reverse('photo_list')	
	"""metodo que permite mostrar el titulo en el administrador de django"""		
	def __str__(self):
		return self.title


class Estudiante(models.Model):
	"""estudiantes"""
	email=models.EmailField(max_length=50)
	nombres=models.CharField(max_length=100,blank=True)
	apellidos=models.CharField(max_length=100,blank=True)
	direccion=models.CharField(max_length=200,blank=True)
	fecha_nac=models.DateField(auto_now_add=False)
	observaciones=models.TextField()
	def __str__(self):
		return self.nombres+" "+self.apellidos